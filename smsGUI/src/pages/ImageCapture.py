from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import *


class ImageCaptureWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageCaptureWidget, self).__init__(parent)

        self.setObjectName("image_capture_page")

        # image_capture_page_layout
        self.image_capture_page_layout = QtWidgets.QGridLayout(self)
        self.image_capture_page_layout.setObjectName("image_capture_page_layout")

        self.camera_layout = QtWidgets.QVBoxLayout()
        self.camera_layout.setContentsMargins(10, 10, 10, 10)
        self.camera_layout.setObjectName("camera_layout")

        self.camera_feed_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_feed_label.sizePolicy().hasHeightForWidth())
        self.camera_feed_label.setSizePolicy(sizePolicy)
        self.camera_feed_label.setMinimumSize(QtCore.QSize(0, 60))
        self.camera_feed_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.camera_feed_label.setObjectName("camera_feed_label")
        self.camera_layout.addWidget(self.camera_feed_label)

        self.video_frame_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_frame_label.sizePolicy().hasHeightForWidth())
        self.video_frame_label.setSizePolicy(sizePolicy)
        self.video_frame_label.setMinimumSize(QtCore.QSize(1024, 576))
        self.video_frame_label.setMaximumSize(QtCore.QSize(1024, 576))
        self.video_frame_label.setAlignment(QtCore.Qt.AlignCenter)
        self.video_frame_label.setObjectName("video_frame_label")
        self.camera_layout.addWidget(self.video_frame_label)

        self.image_capture_page_layout.addLayout(self.camera_layout, 0, 0, 1, 1)

        self.feed_options = QtWidgets.QVBoxLayout()
        self.feed_options.setContentsMargins(10, 10, 10, 10)
        self.feed_options.setObjectName("feed_options")

        spacerItem2 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.feed_options.addItem(spacerItem2)

        self.start_feed_btn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_feed_btn.sizePolicy().hasHeightForWidth())
        self.start_feed_btn.setSizePolicy(sizePolicy)
        self.start_feed_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.start_feed_btn.setMaximumSize(QtCore.QSize(90, 30))
        self.start_feed_btn.setObjectName("start_feed_btn")
        self.feed_options.addWidget(self.start_feed_btn)

        self.end_feed_btn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_feed_btn.sizePolicy().hasHeightForWidth())
        self.end_feed_btn.setSizePolicy(sizePolicy)
        self.end_feed_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.end_feed_btn.setMaximumSize(QtCore.QSize(90, 30))
        self.end_feed_btn.setObjectName("end_feed_btn")
        self.feed_options.addWidget(self.end_feed_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 350, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.feed_options.addItem(spacerItem3)

        self.save_image_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_image_label.sizePolicy().hasHeightForWidth())
        self.save_image_label.setSizePolicy(sizePolicy)
        self.save_image_label.setMinimumSize(QtCore.QSize(0, 40))
        self.save_image_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.save_image_label.setObjectName("save_image_label")
        self.feed_options.addWidget(self.save_image_label)

        self.save_button = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(90, 20))
        self.save_button.setMaximumSize(QtCore.QSize(90, 20))
        self.save_button.setChecked(True)
        self.save_button.setObjectName("save_button")
        self.feed_options.addWidget(self.save_button)

        self.save_as_button = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as_button.sizePolicy().hasHeightForWidth())
        self.save_as_button.setSizePolicy(sizePolicy)
        self.save_as_button.setMinimumSize(QtCore.QSize(90, 20))
        self.save_as_button.setMaximumSize(QtCore.QSize(90, 20))
        self.save_as_button.setObjectName("save_as_button")
        self.feed_options.addWidget(self.save_as_button)

        self.capture_image_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_image_button.sizePolicy().hasHeightForWidth())
        self.capture_image_button.setSizePolicy(sizePolicy)
        self.capture_image_button.setMinimumSize(QtCore.QSize(131, 40))
        self.capture_image_button.setMaximumSize(QtCore.QSize(131, 40))

        self.capture_image_button.setObjectName("capture_image_button")
        self.feed_options.addWidget(self.capture_image_button)

        self.image_capture_page_layout.addLayout(self.feed_options, 0, 1, 1, 1)

        self.image_select_layout = QtWidgets.QGridLayout()
        self.image_select_layout.setContentsMargins(10, 10, 10, 10)
        self.image_select_layout.setObjectName("image_select_layout")

        self.select_image_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_image_label.sizePolicy().hasHeightForWidth())
        self.select_image_label.setSizePolicy(sizePolicy)
        self.select_image_label.setMinimumSize(QtCore.QSize(0, 60))
        self.select_image_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.select_image_label.setObjectName("select_image_label")
        self.image_select_layout.addWidget(self.select_image_label, 0, 0, 1, 2)

        self.select_qr_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_qr_button.sizePolicy().hasHeightForWidth())
        self.select_qr_button.setSizePolicy(sizePolicy)
        self.select_qr_button.setMinimumSize(QtCore.QSize(141, 40))
        self.select_qr_button.setMaximumSize(QtCore.QSize(141, 40))
        self.select_qr_button.setObjectName("select_qr_button")
        self.image_select_layout.addWidget(self.select_qr_button, 1, 0, 1, 1)

        self.qr_path_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qr_path_label.sizePolicy().hasHeightForWidth())
        self.qr_path_label.setSizePolicy(sizePolicy)
        self.qr_path_label.setMinimumSize(QtCore.QSize(150, 30))
        self.qr_path_label.setMaximumSize(QtCore.QSize(150, 30))
        self.qr_path_label.setObjectName("qr_path_label")
        self.image_select_layout.addWidget(self.qr_path_label, 1, 1, 1, 1)

        self.qr_path = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qr_path.sizePolicy().hasHeightForWidth())
        self.qr_path.setSizePolicy(sizePolicy)
        self.qr_path.setMinimumSize(QtCore.QSize(1050, 30))
        self.qr_path.setMaximumSize(QtCore.QSize(1050, 30))
        self.qr_path.setObjectName("qr_path")
        self.image_select_layout.addWidget(self.qr_path, 1, 2, 1, 1)

        self.select_barcode_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_barcode_button.sizePolicy().hasHeightForWidth())
        self.select_barcode_button.setSizePolicy(sizePolicy)
        self.select_barcode_button.setMinimumSize(QtCore.QSize(141, 40))
        self.select_barcode_button.setMaximumSize(QtCore.QSize(141, 40))
        self.select_barcode_button.setObjectName("select_barcode_button")
        self.image_select_layout.addWidget(self.select_barcode_button, 2, 0, 1, 1)

        self.barcode_path_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_path_label.sizePolicy().hasHeightForWidth())
        self.barcode_path_label.setSizePolicy(sizePolicy)
        self.barcode_path_label.setMinimumSize(QtCore.QSize(150, 30))
        self.barcode_path_label.setMaximumSize(QtCore.QSize(150, 30))
        self.barcode_path_label.setObjectName("barcode_path_label")
        self.image_select_layout.addWidget(self.barcode_path_label, 2, 1, 1, 1)

        self.barcode_path = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_path.sizePolicy().hasHeightForWidth())
        self.barcode_path.setSizePolicy(sizePolicy)
        self.barcode_path.setMinimumSize(QtCore.QSize(1050, 30))
        self.barcode_path.setMaximumSize(QtCore.QSize(1050, 30))
        self.barcode_path.setObjectName("barcode_path")
        self.image_select_layout.addWidget(self.barcode_path, 2, 2, 1, 1)

        self.image_capture_page_layout.addLayout(self.image_select_layout, 1, 0, 1, 2)



        # translate image_capture_page
        self.translatePage()

        # link buttons
        self.select_qr_button.clicked.connect(lambda: self.open_file_dialog(0))
        self.select_barcode_button.clicked.connect(lambda: self.open_file_dialog(1))

    # script that updates the qr/barcode path labels with actual image paths
    def open_file_dialog(self, image_type):
        options = QFileDialog.Options()

        # prompt depends on the type of image being selected
        prompt = None
        if image_type == 0:
            prompt = 'Select a QR Code Image'
        elif image_type == 1:
            prompt = 'Select a Barcode Image'

        # returns file path and filter string
        filePath, _ = QFileDialog.getOpenFileName(self, prompt, "", "PNG Files (*.png);;All Files (*)", options=options)
        if filePath:
            if image_type == 0:
                self.qr_path.setText(filePath)
            elif image_type == 1:
                self.barcode_path.setText(filePath)

    def translatePage(self):
        _translate = QtCore.QCoreApplication.translate

        self.save_as_button.setText(_translate("MainWindow", "- Save As -"))
        self.save_button.setText(_translate("MainWindow", "- Save -  "))
        self.camera_feed_label.setText(_translate("MainWindow", "o  Camera Live Feed"))
        self.capture_image_button.setText(_translate("MainWindow", "Capture Image"))
        self.video_frame_label.setText(_translate("MainWindow", "- Video Frame -"))
        self.select_image_label.setText(_translate("MainWindow", "o  Select Images for Detection"))
        self.select_qr_button.setText(_translate("MainWindow", "Select Image (QR Code)"))
        self.qr_path_label.setText(_translate("MainWindow", "Image Path (QR Code):"))
        self.qr_path.setText(_translate("MainWindow", "No Image Selected!"))
        self.select_barcode_button.setText(_translate("MainWindow", "Select Image (Barcode)"))
        self.barcode_path_label.setText(_translate("MainWindow", "Image Path (Barcode):"))
        self.barcode_path.setText(_translate("MainWindow", "No Image Selected!"))
        self.start_feed_btn.setText(_translate("MainWindow", "Start Feed"))
        self.end_feed_btn.setText(_translate("MainWindow", "End Feed"))
        self.save_image_label.setText(_translate("MainWindow", "o Capture/Save Image"))
