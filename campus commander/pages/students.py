import sqlite3
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QFormLayout,
    QMessageBox

)


class StudentsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("🎓 Student Management")
        title.setStyleSheet("""
            color:white;
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.search = QLineEdit()
        self.search.textChanged.connect(self.searchStudents)
        self.search.setPlaceholderText("Search Student...")
        layout.addWidget(self.search)

        buttonLayout = QHBoxLayout()

        self.addBtn = QPushButton("➕ Add Student")
        self.addBtn.clicked.connect(self.addStudent)
        self.editBtn = QPushButton("✏ Edit Student")
        self.editBtn.clicked.connect(self.editStudent)
        self.deleteBtn = QPushButton("❌ Delete Student")
        self.deleteBtn.clicked.connect(self.deleteStudent)

        buttonLayout.addWidget(self.addBtn)
        buttonLayout.addWidget(self.editBtn)
        buttonLayout.addWidget(self.deleteBtn)

        layout.addLayout(buttonLayout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "Name",
            "Roll No",
            "Department",
            "Semester"
        ])

        layout.addWidget(self.table)
        self.loadStudents()

    def loadStudents(self):
        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT name, roll, department, semester
                       FROM students
                       """)

        students = cursor.fetchall()

        self.table.setRowCount(len(students))

        for row, student in enumerate(students):
            for column, value in enumerate(student):
                self.table.setItem(row, column, QTableWidgetItem(str(value)))

        conn.close()

    def searchStudents(self, text):
        text = text.lower()

        for row in range(self.table.rowCount()):
            match = False

            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)

                if item and text in item.text().lower():
                    match = True
                    break

            self.table.setRowHidden(row, not match)

    def addStudent(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Student")

        layout = QFormLayout(dialog)

        name = QLineEdit()
        roll = QLineEdit()
        department = QLineEdit()
        semester = QLineEdit()

        layout.addRow("Name:", name)
        layout.addRow("Roll No:", roll)
        layout.addRow("Department:", department)
        layout.addRow("Semester:", semester)

        saveBtn = QPushButton("Save Student")
        layout.addRow(saveBtn)

    def editStudent(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select a student first."
            )
            return

        old_roll = self.table.item(row, 1).text()

        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Student")

        layout = QFormLayout(dialog)

        name = QLineEdit(self.table.item(row, 0).text())
        roll = QLineEdit(self.table.item(row, 1).text())
        department = QLineEdit(self.table.item(row, 2).text())
        semester = QLineEdit(self.table.item(row, 3).text())

        layout.addRow("Name:", name)
        layout.addRow("Roll No:", roll)
        layout.addRow("Department:", department)
        layout.addRow("Semester:", semester)

        updateBtn = QPushButton("Update Student")
        layout.addRow(updateBtn)

        def update():
            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute("""
                           UPDATE students
                           SET name=?,
                               roll=?,
                               department=?,
                               semester=?
                           WHERE roll = ?
                           """, (
                               name.text(),
                               roll.text(),
                               department.text(),
                               semester.text(),
                               old_roll
                           ))

            conn.commit()
            conn.close()

            self.loadStudents()

            dialog.accept()

        updateBtn.clicked.connect(update)

        dialog.exec()

    def deleteStudent(self):
        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select a student first."
            )
            return

        roll = self.table.item(row, 1).text()

        reply = QMessageBox.question(
            self,
            "Delete Student",
            f"Are you sure you want to delete {roll}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM students WHERE roll=?",
                (roll,)
            )

            conn.commit()
            conn.close()

            self.loadStudents()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Student deleted successfully!"
            )

