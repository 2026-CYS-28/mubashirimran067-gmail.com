import sqlite3

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QHeaderView
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class GradesPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("📊 Grades Management")

        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:white;
            padding:10px;
        """)

        layout.addWidget(title)

        topLayout = QHBoxLayout()

        self.search = QLineEdit()

        self.search.setPlaceholderText("Search Student...")

        self.search.textChanged.connect(
            self.searchGrades
        )

        topLayout.addWidget(self.search)

        self.addBtn = QPushButton("➕ Add Grade")
        self.editBtn = QPushButton("✏ Edit")
        self.deleteBtn = QPushButton("🗑 Delete")

        buttonStyle = """
        QPushButton{
            background:#2563EB;
            color:white;
            border:none;
            border-radius:10px;
            padding:10px;
            font-size:14px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#3B82F6;
        }
        """

        self.addBtn.setStyleSheet(buttonStyle)
        self.editBtn.setStyleSheet(buttonStyle)
        self.deleteBtn.setStyleSheet(buttonStyle)

        self.addBtn.clicked.connect(self.addGrade)
        self.editBtn.clicked.connect(self.editGrade)
        self.deleteBtn.clicked.connect(self.deleteGrade)

        topLayout.addWidget(self.addBtn)
        topLayout.addWidget(self.editBtn)
        topLayout.addWidget(self.deleteBtn)

        layout.addLayout(topLayout)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Student",
            "Roll No",
            "Subject",
            "Marks",
            "Grade"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(self.table)

        self.loadGrades()

    def loadGrades(self):

        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT student, roll, subject, marks, grade
                       FROM grades
                       """)

        grades = cursor.fetchall()

        self.table.setRowCount(len(grades))

        for row, grade in enumerate(grades):

            for column, value in enumerate(grade):

                item = QTableWidgetItem(str(value))

                if column == 4:

                    if value == "A+":
                        item.setBackground(QColor("#16A34A"))

                    elif value == "A":
                        item.setBackground(QColor("#22C55E"))

                    elif value == "B":
                        item.setBackground(QColor("#3B82F6"))

                    elif value == "C":
                        item.setBackground(QColor("#FACC15"))

                    elif value == "D":
                        item.setBackground(QColor("#FB923C"))

                    else:
                        item.setBackground(QColor("#DC2626"))

                self.table.setItem(row, column, item)

        conn.close()

    def searchGrades(self, text):

        text = text.lower()

        for row in range(self.table.rowCount()):

            match = False

            for column in range(self.table.columnCount()):

                item = self.table.item(row, column)

                if item and text in item.text().lower():
                    match = True

            self.table.setRowHidden(row, not match)

    def calculateGrade(self, marks):

        marks = int(marks)

        if marks >= 90:
            return "A+"

        elif marks >= 80:
            return "A"

        elif marks >= 70:
            return "B"

        elif marks >= 60:
            return "C"

        elif marks >= 50:
            return "D"

        else:
            return "F"

    def addGrade(self):

        dialog = QDialog(self)

        dialog.setWindowTitle("Add Grade")

        layout = QFormLayout(dialog)

        student = QLineEdit()
        roll = QLineEdit()
        subject = QLineEdit()
        marks = QLineEdit()

        layout.addRow("Student:", student)
        layout.addRow("Roll No:", roll)
        layout.addRow("Subject:", subject)
        layout.addRow("Marks:", marks)

        saveBtn = QPushButton("Save Grade")

        layout.addRow(saveBtn)

        def save():

            if (
                    not student.text().strip()
                    or not roll.text().strip()
                    or not subject.text().strip()
                    or not marks.text().strip()
            ):
                QMessageBox.warning(
                    self,
                    "Campus Commander",
                    "Please fill all fields."
                )

                return

            try:
                marksValue = int(marks.text())

            except:

                QMessageBox.warning(
                    self,
                    "Campus Commander",
                    "Marks must be a number."
                )

                return

            if marksValue < 0 or marksValue > 100:
                QMessageBox.warning(
                    self,
                    "Campus Commander",
                    "Marks must be between 0 and 100."
                )

                return

            grade = self.calculateGrade(marksValue)

            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute("""
                           INSERT INTO grades(student,
                                              roll,
                                              subject,
                                              marks,
                                              grade)
                           VALUES (?, ?, ?, ?, ?)
                           """, (
                               student.text(),
                               roll.text(),
                               subject.text(),
                               marksValue,
                               grade
                           ))

            conn.commit()
            conn.close()

            self.loadGrades()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Grade added successfully!"
            )

            dialog.accept()

        saveBtn.clicked.connect(save)

        dialog.exec()

    def editGrade(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select a grade first."
            )

            return

        oldRoll = self.table.item(row, 1).text()
        oldSubject = self.table.item(row, 2).text()

        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Grade")

        layout = QFormLayout(dialog)

        student = QLineEdit(self.table.item(row, 0).text())
        roll = QLineEdit(self.table.item(row, 1).text())
        subject = QLineEdit(self.table.item(row, 2).text())
        marks = QLineEdit(self.table.item(row, 3).text())

        layout.addRow("Student:", student)
        layout.addRow("Roll No:", roll)
        layout.addRow("Subject:", subject)
        layout.addRow("Marks:", marks)

        updateBtn = QPushButton("Update Grade")

        layout.addRow(updateBtn)

        def update():

            if (
                    not student.text().strip()
                    or not roll.text().strip()
                    or not subject.text().strip()
                    or not marks.text().strip()
            ):
                QMessageBox.warning(
                    self,
                    "Campus Commander",
                    "Please fill all fields."
                )
                return

            try:
                marksValue = int(marks.text())

            except:

                QMessageBox.warning(
                    self,
                    "Campus Commander",
                    "Marks must be numeric."
                )
                return

            if marksValue < 0 or marksValue > 100:
                QMessageBox.warning(
                    self,
                    "Campus Commander",
                    "Marks must be between 0 and 100."
                )
                return

            grade = self.calculateGrade(marksValue)

            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute("""
                           UPDATE grades
                           SET student=?,
                               roll=?,
                               subject=?,
                               marks=?,
                               grade=?
                           WHERE roll = ?
                             AND subject = ?
                           """, (
                               student.text(),
                               roll.text(),
                               subject.text(),
                               marksValue,
                               grade,
                               oldRoll,
                               oldSubject
                           ))

            conn.commit()
            conn.close()

            self.loadGrades()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Grade updated successfully!"
            )

            dialog.accept()

        updateBtn.clicked.connect(update)

        dialog.exec()

    def deleteGrade(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select a grade first."
            )
            return

        roll = self.table.item(row, 1).text()
        subject = self.table.item(row, 2).text()

        reply = QMessageBox.question(
            self,
            "Delete Grade",
            f"Delete grade for\n\n{roll}\n{subject} ?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute("""
                           DELETE
                           FROM grades
                           WHERE roll = ?
                             AND subject = ?
                           """, (
                               roll,
                               subject
                           ))

            conn.commit()
            conn.close()

            self.loadGrades()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Grade deleted successfully!"
            )


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    window = GradesPage()

    window.resize(1200, 700)

    window.show()

    app.exec()