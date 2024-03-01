from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 679)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # build title frame
        self.title_frame = QtWidgets.QFrame(self.centralwidget)
        self.title_frame.setGeometry(QtCore.QRect(0, 0, 211, 61))
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")

        # place company and application name within title frame
        self.company_title_1 = QtWidgets.QLabel(self.title_frame)
        self.company_title_1.setGeometry(QtCore.QRect(10, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.company_title_1.setFont(font)
        self.company_title_1.setObjectName("company_title_1")
        self.company_title_2 = QtWidgets.QLabel(self.title_frame)
        self.company_title_2.setGeometry(QtCore.QRect(10, 30, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.company_title_2.setFont(font)
        self.company_title_2.setObjectName("company_title_2")

        # menu widget for where the sidebar buttons will be placed
        self.menu_widget = QtWidgets.QListWidget(self.centralwidget)
        self.menu_widget.setGeometry(QtCore.QRect(0, 60, 211, 591))
        self.menu_widget.setObjectName("menu_widget")

        # build sidebar buttons corresponding to the GUI's different windows
        self.button_image_capture = QtWidgets.QPushButton(self.centralwidget)
        self.button_image_capture.setGeometry(QtCore.QRect(0, 80, 211, 51))
        self.button_image_capture.setObjectName("button_image_capture")
        self.button_detection = QtWidgets.QPushButton(self.centralwidget)
        self.button_detection.setGeometry(QtCore.QRect(0, 130, 211, 51))
        self.button_detection.setObjectName("button_detection")
        self.button_report = QtWidgets.QPushButton(self.centralwidget)
        self.button_report.setGeometry(QtCore.QRect(0, 180, 211, 51))
        self.button_report.setObjectName("button_report")
        self.button_help = QtWidgets.QPushButton(self.centralwidget)
        self.button_help.setGeometry(QtCore.QRect(0, 230, 211, 51))
        self.button_help.setObjectName("button_help")

        # build stacked widget for different GUI windows
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 60, 841, 581))
        self.stackedWidget.setObjectName("stackedWidget")

        # build image capture window
        self.image_capture_page = QtWidgets.QWidget()
        self.image_capture_page.setObjectName("image_capture_page")
        self.stackedWidget.addWidget(self.image_capture_page)

        # build image capture label (FOR PURPOSE OF IDENTIFYING DIFFERENT WINDOWS)
        self.image_capture_label = QtWidgets.QLabel(self.image_capture_page)
        self.image_capture_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.image_capture_label.setFont(font)
        self.image_capture_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_capture_label.setObjectName("image_capture_label")

        # build detection page
        self.detection_page = QtWidgets.QWidget()
        self.detection_page.setObjectName("detection_page")
        self.stackedWidget.addWidget(self.detection_page)

        # build detection label (FOR PURPOSE OF IDENTIFYING DIFFERENT WINDOWS)
        self.detection_label = QtWidgets.QLabel(self.detection_page)
        self.detection_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.detection_label.setFont(font)
        self.detection_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detection_label.setObjectName("detection_label")

        # build report page
        self.generate_report_page = QtWidgets.QWidget()
        self.generate_report_page.setObjectName("generate_report_page")
        self.stackedWidget.addWidget(self.generate_report_page)

        # build report label (FOR PURPOSE OF IDENTIFYING DIFFERENT WINDOWS)
        self.report_label = QtWidgets.QLabel(self.generate_report_page)
        self.report_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.report_label.setFont(font)
        self.report_label.setAlignment(QtCore.Qt.AlignCenter)
        self.report_label.setObjectName("report_label")

        # build help page
        self.help_page = QtWidgets.QWidget()
        self.help_page.setObjectName("help_page")
        self.stackedWidget.addWidget(self.help_page)

        # build help label (FOR PURPOSE OF IDENTIFYING DIFFERENT WINDOWS)
        self.help_label = QtWidgets.QLabel(self.help_page)
        self.help_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.help_label.setFont(font)
        self.help_label.setAlignment(QtCore.Qt.AlignCenter)
        self.help_label.setObjectName("help_label")

        # add help window to stacked widgets and
        MainWindow.setCentralWidget(self.centralwidget)

        # status bar on bottom of window
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # set text of window
        self.windowText(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connect sidebar buttons to their respective widgets within the stacked widget
        self.button_image_capture.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.image_capture_page))
        self.button_detection.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.detection_page))
        self.button_report.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.generate_report_page))
        self.button_help.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.help_page))

    def windowText(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "SMS InfoComm Motherboard Inspection"))
        self.company_title_1.setText(_translate("MainWindow", "SMS InfoComm"))
        self.company_title_2.setText(_translate("MainWindow", "Motherboard Inspection"))
        self.button_image_capture.setText(_translate("MainWindow", "Image Capture"))
        self.button_detection.setText(_translate("MainWindow", "Detection"))
        self.button_report.setText(_translate("MainWindow", "Generate Report"))
        self.button_help.setText(_translate("MainWindow", "Help"))
        self.image_capture_label.setText(_translate("MainWindow", "IMAGE CAPTURE PAGE"))
        self.detection_label.setText(_translate("MainWindow", "DETECTION PAGE"))
        self.report_label.setText(_translate("MainWindow", "REPORT PAGE"))
        self.help_label.setText(_translate("MainWindow", "HELP PAGE"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # establish a main window for gui
    MainWindow = QtWidgets.QMainWindow()

    # run main window through setup
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # display main window
    MainWindow.show()
    sys.exit(app.exec_())
