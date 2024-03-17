import cv2
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
import os
from pages.ImageCapture import ImageCaptureWidget
from pages.Detection import DetectionWidget
from pages.Report import ReportWidget
from pages.Help import HelpWidget
from pages.VideoCapture import VideoThread
import faulthandler



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)

        # MainWindow\centralwidget (includes layout)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # MainWindow\centralwidget\sidebar_frame (includes layout)
        self.sidebar_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_frame.setMinimumSize(QtCore.QSize(180, 720))
        self.sidebar_frame.setMaximumSize(QtCore.QSize(180, 16777215))
        self.sidebar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_frame.setObjectName("sidebar_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_frame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")

        # MainWindow\centralwidget\sidebar_frame\company_name
        self.company_name = QtWidgets.QLabel(self.sidebar_frame)
        self.company_name.setObjectName("company_name")
        self.verticalLayout.addWidget(self.company_name)

        # MainWindow\centralwidget\sidebar_frame\app_name
        self.app_name = QtWidgets.QLabel(self.sidebar_frame)
        self.app_name.setObjectName("app_name")
        self.verticalLayout.addWidget(self.app_name)

        # MainWindow\centralwidget\sidebar_frame\sidebar_spacer
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        # MainWindow\centralwidget\sidebar_frame\image_capture_button
        self.image_capture_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.image_capture_button.setMinimumSize(QtCore.QSize(0, 40))
        self.image_capture_button.setObjectName("image_capture_button")
        self.verticalLayout.addWidget(self.image_capture_button)

        # MainWindow\centralwidget\sidebar_frame\detection_button
        self.detection_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.detection_button.setMinimumSize(QtCore.QSize(0, 40))
        self.detection_button.setObjectName("detection_button")
        self.verticalLayout.addWidget(self.detection_button)

        # MainWindow\centralwidget\sidebar_frame\generate_report_button
        self.generate_report_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.generate_report_button.setMinimumSize(QtCore.QSize(0, 40))
        self.generate_report_button.setObjectName("generate_report_button")
        self.verticalLayout.addWidget(self.generate_report_button)

        # MainWindow\centralwidget\sidebar_frame\help_button
        self.help_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.help_button.setMinimumSize(QtCore.QSize(0, 40))
        self.help_button.setObjectName("help_button")
        self.verticalLayout.addWidget(self.help_button)

        # MainWindow\centralwidget\sidebar_frame\sidebar_spacer
        spacerItem1 = QtWidgets.QSpacerItem(20, 443, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        # add sidebar to centralwidget grid layout
        self.gridLayout.addWidget(self.sidebar_frame, 0, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")

        # MainWindow\centralwidget\stackedWidget\image_capture_page
        self.image_capture_page = ImageCaptureWidget()
        # add image_capture_page to stackedWidget
        self.stackedWidget.addWidget(self.image_capture_page)

        # MainWindow\centralwidget\stackedWidget\detection_page (includes layout)
        self.detection_page = DetectionWidget()
        # add detection_page to stackedWidget
        self.stackedWidget.addWidget(self.detection_page)

        # MainWindow\centralwidget\stackedWidget\generate_report_page (includes layout)
        self.generate_report_page = ReportWidget()
        # add generate_report_page to stackedWidget
        self.stackedWidget.addWidget(self.generate_report_page)

        # MainWindow\centralwidget\stackedWidget\help_page (includes layout)
        self.help_page = HelpWidget()
        # add help_page to stackedWidget
        self.stackedWidget.addWidget(self.help_page)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        # set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        # translate GUI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # set initial stackedWidget window
        self.stackedWidget.setCurrentIndex(0)

        # create image folder if it does not yet exist
        self.image_folder()

        # connect sidebar buttons to their respective widgets within the stacked widget
        self.image_capture_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.image_capture_page))
        self.detection_button.clicked.connect(lambda: self.to_detection_check())
        self.generate_report_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.generate_report_page))
        self.help_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.help_page))

        # link restart_program_button with program flow
        self.generate_report_page.restart_program_button.clicked.connect(lambda: self.restart())

        # declare video thread, but instantiate when starting or restarting thread
        self.check_camera()
        self.video_thread = None

        # link video feed buttons
        self.image_capture_page.start_feed_btn.clicked.connect(self.start_video)
        self.image_capture_page.end_feed_btn.clicked.connect(self.stop_video)
        self.image_capture_page.capture_image_button.clicked.connect(self.capture_frame)

    def start_video(self):
        # instantiate thread
        if self.video_thread is None or not self.video_thread.isRunning():
            self.video_thread = VideoThread()
            # connect signals with slots and start video capture
            self.video_thread.update_pixmap_signal.connect(self.update_image)
            self.video_thread.finished_signal.connect(self.video_finished)
            self.video_thread.start()

    # checks for thread activity before stopping thread
    def stop_video(self):
        if self.video_thread is not None and self.video_thread.isRunning():
            self.video_thread.stop()

    def update_image(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        flipImage = cv2.flip(image, 1)
        convertToQt = QImage(flipImage.data, flipImage.shape[1], flipImage.shape[0], QImage.Format_RGB888)
        pic = convertToQt.scaled(1280, 720, Qt.KeepAspectRatio)
        self.image_capture_page.video_frame_label.setPixmap(QPixmap.fromImage(pic))

    def video_finished(self):
        self.image_capture_page.video_frame_label.setText('- Video Frame -')

    def capture_frame(self):
        if self.video_thread is not None and self.video_thread.isRunning():
            # check whether image capture should be 'save' or 'save as'
            save_file = self.image_capture_page.save_button.isChecked()
            self.video_thread.capture_frame(save_file)

    # disables feed buttons if camera device does not exist
    def check_camera(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            self.image_capture_page.start_feed_btn.setDisabled(True)
            self.image_capture_page.end_feed_btn.setDisabled(True)
            self.image_capture_page.video_frame_label.setText('- Video Frame -\nNo Camera Detected!')
            self.image_capture_page.capture_image_button.setDisabled(True)
        cap.release()

    # checks whether a directory for captured images already exists before making one
    @staticmethod
    def image_folder():

        image_folder_name = 'GUI Images'
        image_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), image_folder_name)
        try:
            os.mkdir(image_folder_path)
        except FileExistsError:
            pass

    # checks whether qr code/barcode images exist before entering detection page
    def to_detection_check(self):

        # warning message box in case image paths do not exist
        no_image_warning = QMessageBox(MainWindow)
        no_image_warning.setWindowTitle('Image Selection Error')
        no_image_warning.setText('Please check that you have selected images for both the QR code and \n'
                                 'barcode before entering the detection window.')
        no_image_warning.setIcon(QMessageBox.Critical)
        no_image_warning.setStandardButtons(QMessageBox.Ok)

        # check for existing image paths
        qr = self.image_capture_page.qr_path.text()
        barcode = self.image_capture_page.barcode_path.text()
        if os.path.exists(qr) and os.path.exists(barcode):
            self.stackedWidget.setCurrentWidget(self.detection_page)
        else:
            no_image_warning.exec_()
            pass

    def restart(self):

        # confirmation message box
        confirm_restart = QMessageBox(MainWindow)
        confirm_restart.setWindowTitle('Confirm Program Restart')
        confirm_restart.setText('Would you like to inspect a different motherboard?')
        confirm_restart.setIcon(QMessageBox.Warning)
        confirm_restart.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # check for user response to confirmation message box
        if confirm_restart.exec_() == QMessageBox.Ok:

            # set stacked widget to image capture and clear image files to restart program flow
            self.stackedWidget.setCurrentWidget(self.image_capture_page)
            self.image_capture_page.qr_path.setText('No Image Selected!')
            self.image_capture_page.barcode_path.setText('No Image Selected!')
        else:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SMS Demo Gui V10"))
        self.company_name.setText(_translate("MainWindow", "SMS InfoComm"))
        self.app_name.setText(_translate("MainWindow", "Motherboard Inspection"))
        self.image_capture_button.setText(_translate("MainWindow", "Image Capture"))
        self.detection_button.setText(_translate("MainWindow", "Detection"))
        self.generate_report_button.setText(_translate("MainWindow", "Generate Report"))
        self.help_button.setText(_translate("MainWindow", "Help!"))


if __name__ == "__main__":
    import sys

    faulthandler.enable()

    app = QtWidgets.QApplication(sys.argv)

    # Load style file
    with open("style.qss") as f:
        style_str = f.read()
    app.setStyleSheet(style_str)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
