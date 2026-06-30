import os

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox
)

from PySide6.QtCore import Qt


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("⚙ Settings")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:white;
            padding:15px;
        """)

        layout.addWidget(title)

        self.darkBtn = QPushButton("🌙 Dark Mode")
        self.lightBtn = QPushButton("☀ Light Mode")
        self.aboutBtn = QPushButton("ℹ About")
        self.exitBtn = QPushButton("🚪 Exit Application")

        buttonStyle = """
        QPushButton{
            background:#2563EB;
            color:white;
            border:none;
            border-radius:12px;
            padding:14px;
            font-size:16px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#3B82F6;
        }
        """

        self.darkBtn.setStyleSheet(buttonStyle)
        self.lightBtn.setStyleSheet(buttonStyle)
        self.aboutBtn.setStyleSheet(buttonStyle)
        self.exitBtn.setStyleSheet(buttonStyle)

        layout.addWidget(self.darkBtn)
        layout.addWidget(self.lightBtn)
        layout.addWidget(self.aboutBtn)
        layout.addWidget(self.exitBtn)

        layout.addStretch()

        self.darkBtn.clicked.connect(self.darkMode)
        self.lightBtn.clicked.connect(self.lightMode)
        self.aboutBtn.clicked.connect(self.about)
        self.exitBtn.clicked.connect(self.closeProgram)

    def darkMode(self):

        if os.path.exists("style.qss"):

            with open("style.qss", "r") as file:
                self.window().setStyleSheet(file.read())

        QMessageBox.information(
            self,
            "Campus Commander",
            "Dark mode enabled."
        )

    def lightMode(self):

        self.window().setStyleSheet("")

        QMessageBox.information(
            self,
            "Campus Commander",
            "Light mode enabled."
        )

    def about(self):

        QMessageBox.information(
            self,
            "About Campus Commander",
            """
Campus Commander

Version: 1.0

Developed Using:
• Python
• PySide6
• SQLite

Features

✓ Student Management
✓ Teacher Management
✓ Course Management
✓ Assignment Management
✓ Grade Management
✓ Time Table Management
✓ Dashboard
✓ Login System

Programming Fundamentals Project

University of Engineering and Technology (UET)
"""
        )

    def closeProgram(self):

        reply = QMessageBox.question(
            self,
            "Exit",
            "Are you sure you want to exit Campus Commander?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.window().close()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    window = SettingsPage()
    window.resize(1200, 700)
    window.show()

    app.exec()
