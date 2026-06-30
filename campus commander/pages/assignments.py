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
    QHeaderView,
    QComboBox,
    QDateEdit
)
from datetime import datetime
from PySide6.QtCore import Qt,QDate
from PySide6.QtGui import QColor


class AssignmentsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("📝 Assignment Management")
        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:white;
            padding:10px;
        """)

        layout.addWidget(title)

        topLayout = QHBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Assignment...")
        self.search.textChanged.connect(self.searchAssignments)

        self.search.setStyleSheet("""
            QLineEdit{
                padding:10px;
                border-radius:10px;
                font-size:15px;
            }
        """)
        self.filterBox = QComboBox()

        self.filterBox.addItems([
            "All",
            "Pending",
            "Submitted",
            "Late"
        ])

        self.filterBox.currentTextChanged.connect(
            self.filterAssignments
        )

        topLayout.addWidget(self.filterBox)

        topLayout.addWidget(self.search)

        self.addBtn = QPushButton("+ Add Assignment")
        self.editBtn = QPushButton("✏ Edit")
        self.deleteBtn = QPushButton("🗑 Delete")
        self.sortBtn = QPushButton("📅sort")

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
        self.sortBtn.setStyleSheet(buttonStyle)

        self.addBtn.clicked.connect(self.addAssignment)
        self.editBtn.clicked.connect(self.editAssignment)
        self.deleteBtn.clicked.connect(self.deleteAssignment)
        self.sortBtn.clicked.connect(self.sortAssignments)

        topLayout.addWidget(self.addBtn)
        topLayout.addWidget(self.editBtn)
        topLayout.addWidget(self.deleteBtn)
        topLayout.addWidget(self.sortBtn)

        layout.addLayout(topLayout)

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels([
            "Assignment",
            "Subject",
            "Due Date",
            "Status"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(self.table)

        self.loadAssignments()

    def loadAssignments(self):

        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT assignment, subject, due_date, status
                       FROM assignments
                       """)

        assignments = cursor.fetchall()
        today = datetime.today().date()

        for assignment in assignments:

            assignmentName = assignment[0]
            dueDate = assignment[2]
            status = assignment[3]

            try:
                due = datetime.strptime(dueDate, "%d-%m-%Y").date()

                if due < today and status == "Pending":
                    cursor.execute("""
                                   UPDATE assignments
                                   SET status='Late'
                                   WHERE assignment = ?
                                   """, (assignmentName,))

            except:
                pass

        conn.commit()

        cursor.execute("""
                       SELECT assignment, subject, due_date, status
                       FROM assignments
                       """)

        assignments = cursor.fetchall()

        self.table.setRowCount(len(assignments))

        for row, assignment in enumerate(assignments):

            for column, value in enumerate(assignment):

                item = QTableWidgetItem(str(value))

                if column == 3:

                    if value == "Submitted":
                        item.setBackground(QColor("#16A34A"))

                    elif value == "Pending":
                        item.setBackground(QColor("#FACC15"))

                    elif value == "Late":
                        item.setBackground(QColor("#DC2626"))

                self.table.setItem(row, column, item)

        conn.close()

    def searchAssignments(self, text):

        text = text.lower()

        for row in range(self.table.rowCount()):

            match = False

            for column in range(self.table.columnCount()):

                item = self.table.item(row, column)

                if item and text in item.text().lower():
                    match = True

            self.table.setRowHidden(row, not match)

    def filterAssignments(self, status):

        for row in range(self.table.rowCount()):

            item = self.table.item(row, 3)

            if status == "All":
                self.table.setRowHidden(row, False)

            elif item.text() == status:
                self.table.setRowHidden(row, False)

            else:
                self.table.setRowHidden(row, True)

    def sortAssignments(self):

        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT assignment,
                              subject,
                              due_date,
                              status
                       FROM assignments
                       """)

        assignments = cursor.fetchall()

        assignments.sort(
            key=lambda x: datetime.strptime(
                x[2],
                "%d-%m-%Y"
            )
        )

        self.table.setRowCount(len(assignments))

        for row, assignment in enumerate(assignments):

            for column, value in enumerate(assignment):

                item = QTableWidgetItem(str(value))

                if column == 3:

                    if value == "Submitted":
                        item.setBackground(QColor("#16A34A"))

                    elif value == "Pending":
                        item.setBackground(QColor("#FACC15"))

                    elif value == "Late":
                        item.setBackground(QColor("#DC2626"))

                self.table.setItem(row, column, item)

        conn.close()

    def addAssignment(self):

        dialog = QDialog(self)
        dialog.setWindowTitle("Add Assignment")

        layout = QFormLayout(dialog)

        assignment = QLineEdit()
        subject = QLineEdit()
        dueDate = QDateEdit()

        dueDate.setCalendarPopup(True)

        dueDate.setDate(QDate.currentDate())

        dueDate.setDisplayFormat("dd-MM-yyyy")

        status = QComboBox()
        status.addItems([
            "Pending",
            "Submitted",
            "Late"
        ])

        layout.addRow("Assignment:", assignment)
        layout.addRow("Subject:", subject)
        layout.addRow("Due Date:", dueDate)
        layout.addRow("Status:", status)

        saveBtn = QPushButton("Save Assignment")
        layout.addRow(saveBtn)

        def save():
            if (
                    not assignment.text().strip()
                    or not subject.text().strip()
            ):
                QMessageBox.warning(
                    self,
                    "Campus Commander",
                    "Please fill all fields."
                )

                return

            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute("""
                           INSERT INTO assignments(assignment,
                                                   subject,
                                                   due_date,
                                                   status)
                           VALUES (?, ?, ?, ?)
                           """, (
                               assignment.text(),
                               subject.text(),
                               dueDate.text(),
                               status.currentText()
                           ))
            conn.commit()
            conn.close()

            self.loadAssignments()

            QMessageBox.information(
                            self,
                            "Campus Commander",
                            "Assignment added successfully!"
                        )

        dialog.accept()

        saveBtn.clicked.connect(save)

        dialog.exec()


    def editAssignment(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select an assignment first."
            )
            return

        oldAssignment = self.table.item(row,0).text()

        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Assignment")

        layout = QFormLayout(dialog)

        assignment = QLineEdit(self.table.item(row,0).text())
        subject = QLineEdit(self.table.item(row,1).text())
        dueDate = QLineEdit(self.table.item(row,2).text())

        status = QComboBox()
        status.addItems([
            "Pending",
            "Submitted",
            "Late"
        ])

        status.setCurrentText(
            self.table.item(row,3).text()
        )

        layout.addRow("Assignment:", assignment)
        layout.addRow("Subject:", subject)
        layout.addRow("Due Date:", dueDate)
        layout.addRow("Status:", status)

        updateBtn = QPushButton("Update Assignment")
        layout.addRow(updateBtn)

        def update():

            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE assignments
                SET
                    assignment=?,
                    subject=?,
                    due_date=?,
                    status=?
                WHERE assignment=?
            """,(
                assignment.text(),
                subject.text(),
                dueDate.text(),
                status.currentText(),
                oldAssignment
            ))

            conn.commit()
            conn.close()

            self.loadAssignments()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Assignment updated successfully!"
            )

            dialog.accept()

        updateBtn.clicked.connect(update)

        dialog.exec()

    def deleteAssignment(self):

        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select an assignment first."
            )
            return

        assignment = self.table.item(row, 0).text()

        reply = QMessageBox.question(
            self,
            "Delete Assignment",
            f"Are you sure you want to delete\n\n{assignment} ?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM assignments WHERE assignment=?",
                (assignment,)
            )

            conn.commit()
            conn.close()

            self.loadAssignments()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Assignment deleted successfully!"
            )


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    window = AssignmentsPage()
    window.resize(1200, 700)
    window.show()

    app.exec()