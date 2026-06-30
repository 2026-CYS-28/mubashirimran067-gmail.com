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
    QComboBox
)


class TimeTablePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("📅 Time Table Management")

        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:white;
            padding:10px;
        """)

        layout.addWidget(title)

        topLayout = QHBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Timetable...")
        self.search.textChanged.connect(self.searchTimeTable)

        topLayout.addWidget(self.search)

        self.addBtn = QPushButton("➕ Add Class")
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

        self.addBtn.clicked.connect(self.addClass)
        self.editBtn.clicked.connect(self.editClass)
        self.deleteBtn.clicked.connect(self.deleteClass)

        topLayout.addWidget(self.addBtn)
        topLayout.addWidget(self.editBtn)
        topLayout.addWidget(self.deleteBtn)

        layout.addLayout(topLayout)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Day",
            "Time",
            "Course",
            "Teacher",
            "Room"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(self.table)

        self.loadTimeTable()

    def loadTimeTable(self):

        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT day, time, course, teacher, room
                       FROM timetable
                       """)

        classes = cursor.fetchall()

        self.table.setRowCount(len(classes))

        for row, data in enumerate(classes):

            for column, value in enumerate(data):
                self.table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )

        conn.close()

    def searchTimeTable(self, text):

        text = text.lower()

        for row in range(self.table.rowCount()):

            match = False

            for column in range(self.table.columnCount()):

                item = self.table.item(row, column)

                if item and text in item.text().lower():
                    match = True

            self.table.setRowHidden(row, not match)

    def addClass(self):

        dialog = QDialog(self)
        dialog.setWindowTitle("Add Class")

        layout = QFormLayout(dialog)

        day = QComboBox()

        day.addItems([
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ])

        time = QLineEdit()
        course = QLineEdit()
        teacher = QLineEdit()
        room = QLineEdit()

        layout.addRow("Day:", day)
        layout.addRow("Time:", time)
        layout.addRow("Course:", course)
        layout.addRow("Teacher:", teacher)
        layout.addRow("Room:", room)

        saveBtn = QPushButton("Save Class")

        layout.addRow(saveBtn)

        def save():
            if (
                    not time.text().strip()
                    or not course.text().strip()
                    or not teacher.text().strip()
                    or not room.text().strip()
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
                           INSERT INTO timetable(day,
                                                 time,
                                                 course,
                                                 teacher,
                                                 room)
                           VALUES (?, ?, ?, ?, ?)
                           """, (
                               day.currentText(),
                               time.text(),
                               course.text(),
                               teacher.text(),
                               room.text()
                           ))
            conn.commit()
            conn.close()

            self.loadTimeTable()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Class added successfully!"
            )

            dialog.accept()

        saveBtn.clicked.connect(save)

        dialog.exec()


    def editClass(self):

        row = self.table.currentRow()

        if row == -1:

            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select a class first."
            )
            return

        oldDay = self.table.item(row,0).text()
        oldTime = self.table.item(row,1).text()

        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Class")

        layout = QFormLayout(dialog)

        day = QComboBox()

        day.addItems([
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ])

        day.setCurrentText(
            self.table.item(row,0).text()
        )

        time = QLineEdit(self.table.item(row,1).text())
        course = QLineEdit(self.table.item(row,2).text())
        teacher = QLineEdit(self.table.item(row,3).text())
        room = QLineEdit(self.table.item(row,4).text())

        layout.addRow("Day:", day)
        layout.addRow("Time:", time)
        layout.addRow("Course:", course)
        layout.addRow("Teacher:", teacher)
        layout.addRow("Room:", room)

        updateBtn = QPushButton("Update Class")

        layout.addRow(updateBtn)

        def update():

            if (
                not time.text().strip()
                or not course.text().strip()
                or not teacher.text().strip()
                or not room.text().strip()
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
                UPDATE timetable
                SET
                    day=?,
                    time=?,
                    course=?,
                    teacher=?,
                    room=?
                WHERE day=? AND time=?
            """, (
                day.currentText(),
                time.text(),
                course.text(),
                teacher.text(),
                room.text(),
                oldDay,
                oldTime
            ))
            conn.commit()
            conn.close()

            self.loadTimeTable()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Class updated successfully!"
            )

            dialog.accept()

        updateBtn.clicked.connect(update)

        dialog.exec()


    def deleteClass(self):

        row = self.table.currentRow()

        if row == -1:

            QMessageBox.warning(
                self,
                "Campus Commander",
                "Please select a class first."
            )
            return

        day = self.table.item(row,0).text()
        time = self.table.item(row,1).text()

        reply = QMessageBox.question(
            self,
            "Delete Class",
            f"Delete class on\n\n{day} at {time}?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:

            conn = sqlite3.connect("campus.db")
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM timetable
                WHERE day=? AND time=?
            """, (
                day,
                time
            ))

            conn.commit()
            conn.close()

            self.loadTimeTable()

            QMessageBox.information(
                self,
                "Campus Commander",
                "Class deleted successfully!"
            )


if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    window = TimeTablePage()

    window.resize(1200,700)

    window.show()

    app.exec()
