from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QScrollArea,

)
from PySide6.QtCore import Qt

from pages.dashboard import DashboardPage
from pages.time_table import TimeTablePage
from pages.grades import GradesPage
from pages.assignments import AssignmentsPage
from pages.settings import SettingsPage
from pages.students import StudentsPage


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("campus commander")
        self.showMaximized()
        self.resize(1300,800)

        mainLayout=QHBoxLayout(self)

        # Sidebar

        sidebarWidget = QWidget()
        sidebarWidget.setFixedWidth(280)

        sidebar = QVBoxLayout(sidebarWidget)
        sidebar.setContentsMargins(20, 20, 20, 20)
        sidebar.setSpacing(15)

        logo = QLabel("CC")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setFixedSize(80, 80)

        logo.setStyleSheet("""
        background:#00D4FF;
        color:white;
        font-size:24px;
        font-weight:bold;
        border-radius:35px;
        """)

        title = QLabel("Campus\nCommander")
        title.setStyleSheet("""
        font-size:22px;
        font-weight:bold;
        color:white;
        """)


        dashboardBtn = QPushButton("🏠  Dashboard")
        timetableBtn = QPushButton("📅  Timetable")
        gradesBtn = QPushButton("📊  Grades")
        assignmentsBtn = QPushButton("📝  Assignments")
        settingsBtn = QPushButton("⚙️  Settings")
        studentsBtn=QPushButton("🎓students")
        buttons = [
            dashboardBtn,
            timetableBtn,
            gradesBtn,
            assignmentsBtn,
            settingsBtn,
            studentsBtn
        ]

        for btn in buttons:
            btn.setMinimumHeight(55)
            btn.setMinimumWidth(230)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton{
                    background:#101A2D;
                    color:white;
                    border:none;
                    border-radius:15px;
                    padding-left:30px;
                    text-align:left;
                    font-size:15px;
                }

                QPushButton:hover{
                    background:#00D4FF;
                    color:black;
                }

                QPushButton:pressed{
                    background:#0099CC;
                }
            """)

        sidebar.addWidget(logo)
        sidebar.addWidget(title)
        sidebar.addSpacing(25)

        sidebar.addWidget(dashboardBtn)
        sidebar.addWidget(timetableBtn)
        sidebar.addWidget(gradesBtn)
        sidebar.addWidget(assignmentsBtn)
        sidebar.addWidget(settingsBtn)
        sidebar.addWidget(studentsBtn)
        sidebar.addStretch()

        # Pages

        self.stack=QStackedWidget()

        self.dashboard=DashboardPage()
        self.timetable=TimeTablePage()
        self.grades=GradesPage()
        self.assignments=AssignmentsPage()
        self.settings=SettingsPage()
        self.students=StudentsPage()

        dashboardScroll = QScrollArea()
        dashboardScroll.setWidgetResizable(True)
        dashboardScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        dashboardScroll.setWidget(self.dashboard)

        self.stack.addWidget(dashboardScroll)
        self.stack.addWidget(self.timetable)
        self.stack.addWidget(self.grades)
        self.stack.addWidget(self.assignments)
        self.stack.addWidget(self.settings)
        self.stack.addWidget(self.students)
        dashboardBtn.clicked.connect(lambda:self.stack.setCurrentIndex(0))
        timetableBtn.clicked.connect(lambda:self.stack.setCurrentIndex(1))
        gradesBtn.clicked.connect(lambda:self.stack.setCurrentIndex(2))
        assignmentsBtn.clicked.connect(lambda:self.stack.setCurrentIndex(3))
        settingsBtn.clicked.connect(lambda:self.stack.setCurrentIndex(4))
        studentsBtn.clicked.connect(lambda:self.stack.setCurrentIndex(5))
        mainLayout.addWidget(sidebarWidget)
        mainLayout.addWidget(self.stack,1)
        self.setLayout(mainLayout)

    def openPageBySearch(self, text):
        text = text.lower().strip()

        if text == "":
            return

        if "dashboard" in text:
            self.stack.setCurrentIndex(0)

        elif "timetable" in text or "schedule" in text:
            self.stack.setCurrentIndex(1)

        elif "grades" in text:
            self.stack.setCurrentIndex(2)

        elif "student" in text or "assignment" in text:
            self.stack.setCurrentIndex(3)

        elif "setting" in text:
            self.stack.setCurrentIndex(4)