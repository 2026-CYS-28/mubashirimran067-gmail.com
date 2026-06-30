import sqlite3

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox,
    QComboBox
)

import database


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Campus Commander Login")
        self.resize(400,420)

        layout = QVBoxLayout()

        title = QLabel("Campus Commander")
        title.setStyleSheet("font-size:24px;font-weight:bold;")

        layout.addWidget(title)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        layout.addWidget(self.password)

        self.role = QComboBox()
        self.role.addItems(["Student","Admin"])

        layout.addWidget(self.role)

        login_btn = QPushButton("Login")
        register_btn = QPushButton("Register")

        layout.addWidget(login_btn)
        layout.addWidget(register_btn)

        login_btn.clicked.connect(self.login)
        register_btn.clicked.connect(self.register)

        self.setLayout(layout)

    def register(self):

        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        try:

            cursor.execute(
                "INSERT INTO users(username,password,role) VALUES(?,?,?)",
                (
                    self.username.text(),
                    self.password.text(),
                    self.role.currentText()
                )
            )

            conn.commit()

            QMessageBox.information(
                self,
                "Success",
                "Registration Successful"
            )

        except:

            QMessageBox.warning(
                self,
                "Error",
                "User already exists"
            )

        conn.close()

    def login(self):

        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=? AND role=?",
            (
                self.username.text(),
                self.password.text(),
                self.role.currentText()
            )
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            QMessageBox.information(
                self,
                "Success",
                "Login Successful"
            )
            from widget.sidebar import MainWindow

            self.window = MainWindow()
            self.window.show()
            self.close()
            # Dashboard will open here later

        else:

            QMessageBox.warning(
                self,
                "Error",
                "Invalid Login"
            )