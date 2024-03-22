import cv2
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from pages.ImageCapture import ImageCaptureWidget
from pages.Detection import DetectionWidget
from pages.Report import ReportWidget
from pages.Help import HelpWidget
from Services.VideoCapture import VideoThread
from Services.ImageComparison import compare_images
from Services.report_generation import create_pdf_with_image
import Services.decodePic as dp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))

        # centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1600, 900))
        self.centralwidget.setObjectName("centralwidget")

        # central_widget_layout
        self.central_widget_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_layout.setObjectName("central_widget_layout")

        # sidebar_frame
        self.sidebar_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_frame.setMinimumSize(QtCore.QSize(180, 900))
        self.sidebar_frame.setMaximumSize(QtCore.QSize(180, 16777215))
        self.sidebar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_frame.setObjectName("sidebar_frame")

        # sidebar_frame_layout
        self.sidebar_frame_layout = QtWidgets.QVBoxLayout(self.sidebar_frame)
        self.sidebar_frame_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.sidebar_frame_layout.setObjectName("sidebar_frame_layout")

        # company name
        self.company_name = QtWidgets.QLabel(self.sidebar_frame)
        self.company_name.setObjectName("company_name")
        self.sidebar_frame_layout.addWidget(self.company_name)

        # app_name
        self.app_name = QtWidgets.QLabel(self.sidebar_frame)
        self.app_name.setObjectName("app_name")
        self.sidebar_frame_layout.addWidget(self.app_name)

        # spacerItem (sidebar spacer)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.sidebar_frame_layout.addItem(spacerItem)

        # image_capture_button
        self.image_capture_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.image_capture_button.setMinimumSize(QtCore.QSize(0, 40))
        self.image_capture_button.setObjectName("image_capture_button")
        self.sidebar_frame_layout.addWidget(self.image_capture_button)

        # detection_button
        self.detection_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.detection_button.setMinimumSize(QtCore.QSize(0, 40))
        self.detection_button.setObjectName("detection_button")
        self.sidebar_frame_layout.addWidget(self.detection_button)

        # generate_report_button
        self.generate_report_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.generate_report_button.setMinimumSize(QtCore.QSize(0, 40))
        self.generate_report_button.setObjectName("generate_report_button")
        self.sidebar_frame_layout.addWidget(self.generate_report_button)

        # help_button
        self.help_button = QtWidgets.QPushButton(self.sidebar_frame)
        self.help_button.setMinimumSize(QtCore.QSize(0, 40))
        self.help_button.setObjectName("help_button")
        self.sidebar_frame_layout.addWidget(self.help_button)

        # spacerItem1 (another sidebar spacer)
        spacerItem1 = QtWidgets.QSpacerItem(20, 443, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebar_frame_layout.addItem(spacerItem1)

        # add sidebar to centralwidget grid layout
        self.central_widget_layout.addWidget(self.sidebar_frame, 0, 0, 1, 1)

        # stackedWidget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1420, 890))
        self.stackedWidget.setObjectName("stackedWidget")

        # build image_capture_page
        self.image_capture_page = ImageCaptureWidget()
        # add image_capture_page to stackedWidget
        self.stackedWidget.addWidget(self.image_capture_page)

        # build detection_page
        self.detection_page = DetectionWidget()
        # add detection_page to stackedWidget
        self.stackedWidget.addWidget(self.detection_page)

        # build generate_report_page
        self.generate_report_page = ReportWidget()
        # add generate_report_page to stackedWidget
        self.stackedWidget.addWidget(self.generate_report_page)

        # build help_page
        self.help_page = HelpWidget()
        # add help_page to stackedWidget
        self.stackedWidget.addWidget(self.help_page)

        # add stacked widget to central widget layout
        self.central_widget_layout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        # set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # translate GUI
        self.retranslateUi(MainWindow)

        # connect pyqt signals and slots
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

        # invoke qr/barcode detection function
        self.detection_page.matrix_recognition_button.clicked.connect(lambda: self.qr_barcode_detection(1))
        self.detection_page.barcode_recognition_button.clicked.connect(lambda: self.qr_barcode_detection(0))
        self.code = None
        # invoke the image comparison function
        self.detection_page.run_comparison_button.clicked.connect(lambda: self.image_comparison())
        # invoke the report generation function
        self.generate_report_page.generate_report_button_2.clicked.connect(lambda: self.gen_report())

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
        pic = convertToQt.scaled(640, 480, Qt.KeepAspectRatio)
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

    # checks whether a directory for captured images and reports already exist before making one
    @staticmethod
    def image_folder():

        image_folder_name = 'GUI Images'
        report_folder_name = "Reports"
        image_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), image_folder_name)
        report_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), report_folder_name)
        try:
            os.mkdir(image_folder)
        except FileExistsError:
            pass
        try:
            os.mkdir(report_folder)
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

        wrong_ext_warning = QMessageBox(MainWindow)
        wrong_ext_warning.setWindowTitle('File Extension Error')
        wrong_ext_warning.setText('Please check that you have selected the right files for detection.')
        wrong_ext_warning.setIcon(QMessageBox.Critical)
        wrong_ext_warning.setStandardButtons(QMessageBox.Ok)

        # check for existing image paths
        qr = self.image_capture_page.qr_path.text()
        print(qr)
        barcode = self.image_capture_page.barcode_path.text()

        if os.path.exists(qr) and os.path.exists(barcode):
            qr_name, qr_ext = os.path.splitext(qr)
            bar_name, bar_ext = os.path.splitext(barcode)
            img_ext = ['.png', '.jpg', '.jpeg']
            if qr_ext.lower() in img_ext and bar_ext.lower() in img_ext:
                self.update_mobo_image(qr, self.detection_page.chosen_image_label)
                self.stackedWidget.setCurrentWidget(self.detection_page)
            else:
                wrong_ext_warning.exec_()
        else:
            no_image_warning.exec_()
            pass

    def update_mobo_image(self, mobo_image, label):
        img = cv2.imread(mobo_image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (640, 360))

        height, width, channel = img.shape
        bytes_per_line = 3 * width
        q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(q_image))

    def qr_barcode_detection(self, is_qr_detection):
        success = None
        self.code = None
        qr_img_path = self.image_capture_page.qr_path.text()
        barcode_img_path = self.image_capture_page.barcode_path.text()
        # IMPORTANT: check whether model names and/or paths have been changed
        qr_model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'best.pt')
        barcode_model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'best_Barcode.pt')
        if os.path.exists(qr_model_path) and os.path.exists(barcode_model_path):
            # run qr detection
            if is_qr_detection:
                success, self.code = dp.decode_main(qr_model_path, qr_img_path, True)
            # run barcode detection
            else:
                success, self.code = dp.decode_main(barcode_model_path, barcode_img_path, False)
            if success:
                self.detection_page.result_ppid.setText(self.code)
                # Send the code to the image comparison function

        # fail-safe for misplaced model files
        else:
            print('The Detection models are misplaced or missing!')

    def image_comparison(self):
        # Finds the location of the Golden Image
        image_folder = "MotherBoard Images"
        golden_subfolder = "Golden Images"
        golden_image_filename = "golden.png"
        golden_image_path = os.path.join(image_folder, golden_subfolder, golden_image_filename)

        # Finds the location of the Defected Image
        defected_subfolder = "Defect Images"
        defected_image_filename = str(self.code + ".png")
        defected_image_path = os.path.join(image_folder, defected_subfolder, defected_image_filename)

        # Compare the image to the golden image
        compare_images(defected_image_path, golden_image_path, align=True, sensitivity_threshold=40, blur_value=(7, 7))

        # Output for the image
        outputImage = "highlighted_output.jpg"

        # Update the Reference Frame and Comparison Frame
        self.update_mobo_image(golden_image_path, self.detection_page.reference_image_label)
        self.update_mobo_image(outputImage, self.detection_page.result_image_label)

    # NOTE: UPDATE ONCE IMAGE PATHS ARE NO LONGER HARD-CODED
    def gen_report(self):
        # first, check whether image paths even exist
        golden_image = 'MotherBoard Images\\Golden Images\\golden.png'
        defect_image = f'MotherBoard Images\\Defect Images\\{self.code}.png'
        comparison_image = 'highlighted_output.jpg'

        if os.path.exists(golden_image) and os.path.exists(defect_image) and os.path.exists(comparison_image):
            create_pdf_with_image(comparison_image, defect_image, golden_image)
        else:
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
            # delete comparison results to prevent report invalid report generation
            self.detection_page.result_image_label.setText('- Result Image Frame -')
            self.detection_page.result_image_label.update()
            self.detection_page.reference_image_label.setText('- Reference Image Frame -')
            self.detection_page.reference_image_label.update()
            try:
                os.remove('highlighted_output.jpg')
            except FileNotFoundError:
                pass
        else:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SMS Demo Gui V11"))
        self.company_name.setText(_translate("MainWindow", "SMS InfoComm"))
        self.app_name.setText(_translate("MainWindow", "Motherboard Inspection"))
        self.image_capture_button.setText(_translate("MainWindow", "Image Capture"))
        self.detection_button.setText(_translate("MainWindow", "Detection"))
        self.generate_report_button.setText(_translate("MainWindow", "Generate Report"))
        self.help_button.setText(_translate("MainWindow", "Help!"))


if __name__ == "__main__":
    import sys

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
