from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QFrame,


)
from PySide6.QtCore import Qt
import sqlite3

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color:#202633;")

        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(30, 30, 30, 30)
        mainLayout.setSpacing(25)

        # ===== Title =====
        welcome = QLabel("Good Evening!!! 👋")

        welcome.setStyleSheet("""
        color:white;
        font-size:30px;
        font-weight:bold;
        """)
        subtitle = QLabel("Welcome back to Campus Commander")

        subtitle.setStyleSheet("""
        color:#8E9AAF;
        font-size:16px;
        """)

        mainLayout.addWidget(welcome)
        mainLayout.addWidget(subtitle)
        mainLayout.addSpacing(20)

        from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton

        topBar = QHBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")
        self.search.textChanged.connect(self.globalSearch)
        self.search.setFixedHeight(40)

        topBar.addWidget(self.search)

        notification = QPushButton("🔔")
        notification.setFixedSize(45, 45)

        profile = QPushButton("👤")
        profile.setFixedSize(45, 45)

        notification.setStyleSheet("""
        QPushButton{
            background:#151C2C;
            border-radius:22px;
            font-size:18px;
        }
        QPushButton:hover{
            background:#00D4FF;
        }
        """)

        profile.setStyleSheet(notification.styleSheet())

        topBar.addWidget(notification)
        topBar.addSpacing(10)
        topBar.addWidget(profile)

        mainLayout.addLayout(topBar)
        mainLayout.addSpacing(20)

        grid = QGridLayout()
        grid.setSpacing(20)

        def createCard(title, value):

            card = QFrame()
            card.setFixedHeight(150)

            card.setStyleSheet("""
            QFrame{
                background:#101A2D;
                border-radius:20px;
            }
            """)

            layout = QVBoxLayout(card)

            valueLabel = QLabel(value)
            valueLabel.setStyleSheet("""
            color:white;
            font-size:32px;
            font-weight:bold;
            """)

            titleLabel = QLabel(title)
            titleLabel.setStyleSheet("""
            color:#8E9AAF;
            font-size:15px;
            """)

            layout.addWidget(valueLabel)
            layout.addWidget(titleLabel)

            return card

        students = createCard("Students", "520")
        teachers = createCard("Teachers", "38")
        courses = createCard("Courses", "26")
        today = createCard("Today's Classes", "14")

        welcome.setStyleSheet("""
            color:white;
            font-size:32px;
            font-weight:bold;
        """)
        mainLayout.addWidget(welcome)
        mainLayout.addWidget(subtitle)
        mainLayout.addSpacing(15)

        from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton
        from PySide6.QtCore import QTimer, QTime

        # ===== Top Bar =====
        topBar = QHBoxLayout()

        clock = QLabel()

        clock.setStyleSheet("""
        color:white;
        font-size:18px;
        font-weight:bold;
        """)

        def updateTime():
            clock.setText(QTime.currentTime().toString("hh:mm:ss AP"))

        timer = QTimer(self)
        timer.timeout.connect(updateTime)
        timer.start(1000)
        updateTime()


        topBar.addStretch()
        topBar.addWidget(clock)

        mainLayout.addLayout(topBar)

        # ===== Cards =====
        grid = QGridLayout()
        grid.setSpacing(20)

        conn = sqlite3.connect("campus.db")
        cursor = conn.cursor()

        student_count = cursor.execute(
            "SELECT COUNT(*) FROM students"
        ).fetchone()[0]

        teacher_count = cursor.execute(
            "SELECT COUNT(*) FROM teachers"
        ).fetchone()[0]

        course_count = cursor.execute(
            "SELECT COUNT(*) FROM courses"
        ).fetchone()[0]

        conn.close()

        data = [
            ("👨 Students", str(student_count)),
            ("🔒 Teachers", str(teacher_count)),
            ("📚 Courses", str(course_count)),
            ("🗓 Attendance", "94%")
        ]
        row = 0
        col = 0

        for name, value in data:

            card = QFrame()
            card.setObjectName(name.lower())
            if not hasattr(self,"cards"):
                self.cards=[]
            card.setFixedSize(280, 170)

            card.setStyleSheet("""
                QFrame{
                    background:#151C2C;
                    border-radius:18px;
                    border:2px solid #26324D;
                }
            """)

            layout = QVBoxLayout(card)

            text = QLabel(name)
            text.setStyleSheet("""
                color:#A5B2D1;
                font-size:18px;
            """)

            number = QLabel(value)
            number.setAlignment(Qt.AlignmentFlag.AlignCenter)
            number.setStyleSheet("""
                color:white;
                font-size:42px;
                font-weight:bold;
            """)

            layout.addWidget(text)
            layout.addStretch()
            layout.addWidget(number)
            layout.addStretch()

            grid.addWidget(card, row, col)
            self.cards.append((name,card))

            col += 1
            if col > 2:
                col = 0
                row += 1

        mainLayout.addLayout(grid)

        mainLayout.addSpacing(25)

        timetableCard = QFrame()

        timetableCard.setStyleSheet("""
        QFrame{
            background:#151C2C;
            border-radius:20px;
            border:2px solid #263240;
        }
        """)

        timetableLayout = QVBoxLayout(timetableCard)
        title = QLabel("📅 Today's Timetable")

        title.setStyleSheet("""
        font-size:22px;
        font-weight:bold;
        color:white;
        """)

        timetableLayout.addWidget(title)

        classes = [
            ("08:30 AM", "Programming Fundamentals"),
            ("10:00 AM", "Calculus"),
            ("01:00 PM", "Cyber Security"),
            ("03:00 PM", "English")
        ]

        for time, subject in classes:
            row = QFrame()
            row.setFixedHeight(50)
            row.setStyleSheet("""
            QFrame{
                background:#101A2D;
                border-radius:12px;
            }
            """)

            rowLayout = QHBoxLayout(row)
            rowLayout.setContentsMargins(15,10,15,10)

            timeLabel = QLabel(time)
            timeLabel.setStyleSheet("""
                color:#00D4FF;
                font-weight:bold;
                font-size:14px;
                background:#1C2A48;
                padding:6px 12px;
                border-radius:8px;
            """)

            subjectLabel = QLabel(subject)
            subjectLabel.setStyleSheet("color:white;")

            rowLayout.addWidget(timeLabel)
            rowLayout.addStretch()
            rowLayout.addWidget(subjectLabel)

            timetableLayout.addWidget(row)

        mainLayout.addWidget(timetableCard)
        mainLayout.addSpacing(20)
        timetableTitle = QLabel("Today's Timetable")
        timetableTitle.setStyleSheet("color:white; font-size:24px; font-weight:bold;")
        mainLayout.addWidget(timetableTitle)
        mainLayout.addSpacing(10)
        mainLayout.addStretch()

    def searchDashboard(self, text):
        text = text.lower().strip()

        if text == "":
            for name, card in self.cards:
                card.show()
            return

        for name, card in self.cards:
            if text in name.lower():
                card.show()
            else:
                card.hide()

    def globalSearch(self, text):
        # Filter dashboard cards
        self.searchDashboard(text)

        # Navigate to pages
        self.window().window().openPageBySearch(text)