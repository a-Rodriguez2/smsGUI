from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os


class ImageCaptureWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageCaptureWidget, self).__init__(parent)

        self.setObjectName("image_capture_page")

        # image_capture_page layout
        self.gridLayout_9 = QtWidgets.QGridLayout(self)
        self.gridLayout_9.setObjectName("gridLayout_9")

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout
        self.camera_layout = QtWidgets.QGridLayout()
        self.camera_layout.setObjectName("camera_layout")

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\save_as_button
        self.save_as_button = QtWidgets.QRadioButton(self)
        self.save_as_button.setObjectName("save_as_button")
        self.camera_layout.addWidget(self.save_as_button, 3, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\save_button
        self.save_button = QtWidgets.QRadioButton(self)
        self.save_button.setChecked(True)
        self.save_button.setObjectName("save_button")
        self.camera_layout.addWidget(self.save_button, 2, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\camera_feed_label
        self.camera_feed_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_feed_label.sizePolicy().hasHeightForWidth())
        self.camera_feed_label.setSizePolicy(sizePolicy)
        self.camera_feed_label.setMinimumSize(QtCore.QSize(0, 60))
        self.camera_feed_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.camera_feed_label.setObjectName("camera_feed_label")
        self.camera_layout.addWidget(self.camera_feed_label, 0, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\capture_image_button
        self.capture_image_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_image_button.sizePolicy().hasHeightForWidth())
        self.capture_image_button.setSizePolicy(sizePolicy)
        self.capture_image_button.setMinimumSize(QtCore.QSize(131, 40))
        self.capture_image_button.setMaximumSize(QtCore.QSize(131, 40))
        self.capture_image_button.setObjectName("capture_image_button")
        self.camera_layout.addWidget(self.capture_image_button, 2, 0, 2, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\video_frame (includes layout)
        self.video_frame = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_frame.sizePolicy().hasHeightForWidth())
        self.video_frame.setSizePolicy(sizePolicy)
        self.video_frame.setMinimumSize(QtCore.QSize(640, 360))
        self.video_frame.setMaximumSize(QtCore.QSize(640, 360))
        self.video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_frame.setObjectName("video_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.video_frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\video_frame\video_frame_label
        self.video_frame_label = QtWidgets.QLabel(self.video_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_frame_label.sizePolicy().hasHeightForWidth())
        self.video_frame_label.setSizePolicy(sizePolicy)
        self.video_frame_label.setAlignment(QtCore.Qt.AlignCenter)
        self.video_frame_label.setObjectName("video_frame_label")
        self.gridLayout_2.addWidget(self.video_frame_label, 0, 1, 1, 1)

        # add video_frame to camera_layout
        self.camera_layout.addWidget(self.video_frame, 1, 0, 1, 2)
        # add camera_layout to image_capture_page
        self.gridLayout_9.addLayout(self.camera_layout, 0, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout
        self.image_manip_layout = QtWidgets.QGridLayout()
        self.image_manip_layout.setObjectName("image_manip_layout")

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\zoom_label
        self.zoom_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_label.sizePolicy().hasHeightForWidth())
        self.zoom_label.setSizePolicy(sizePolicy)
        self.zoom_label.setMinimumSize(QtCore.QSize(380, 50))
        self.zoom_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.zoom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.zoom_label.setObjectName("zoom_label")
        self.image_manip_layout.addWidget(self.zoom_label, 0, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\zoom_slider
        self.zoom_slider = QtWidgets.QSlider(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_slider.sizePolicy().hasHeightForWidth())
        self.zoom_slider.setSizePolicy(sizePolicy)
        self.zoom_slider.setMinimumSize(QtCore.QSize(380, 0))
        self.zoom_slider.setMaximumSize(QtCore.QSize(380, 16777215))
        self.zoom_slider.setSliderPosition(50)
        self.zoom_slider.setOrientation(QtCore.Qt.Horizontal)
        self.zoom_slider.setObjectName("zoom_slider")
        self.image_manip_layout.addWidget(self.zoom_slider, 1, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\image_manip_spacer
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.image_manip_layout.addItem(spacerItem2, 2, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\brightness_label
        self.brightness_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightness_label.sizePolicy().hasHeightForWidth())
        self.brightness_label.setSizePolicy(sizePolicy)
        self.brightness_label.setMinimumSize(QtCore.QSize(380, 50))
        self.brightness_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.brightness_label.setAlignment(QtCore.Qt.AlignCenter)
        self.brightness_label.setObjectName("brightness_label")
        self.image_manip_layout.addWidget(self.brightness_label, 2, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\image_manip_spacer
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.image_manip_layout.addItem(spacerItem3, 2, 2, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\brightness_slider
        self.brightness_slider = QtWidgets.QSlider(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightness_slider.sizePolicy().hasHeightForWidth())
        self.brightness_slider.setSizePolicy(sizePolicy)
        self.brightness_slider.setMaximumSize(QtCore.QSize(380, 16777215))
        self.brightness_slider.setSliderPosition(50)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.image_manip_layout.addWidget(self.brightness_slider, 3, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\contrast_label
        self.contrast_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contrast_label.sizePolicy().hasHeightForWidth())
        self.contrast_label.setSizePolicy(sizePolicy)
        self.contrast_label.setMinimumSize(QtCore.QSize(380, 50))
        self.contrast_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.contrast_label.setAlignment(QtCore.Qt.AlignCenter)
        self.contrast_label.setObjectName("contrast_label")
        self.image_manip_layout.addWidget(self.contrast_label, 4, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_manip_layout\contrast_slider
        self.contrast_slider = QtWidgets.QSlider(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contrast_slider.sizePolicy().hasHeightForWidth())
        self.contrast_slider.setSizePolicy(sizePolicy)
        self.contrast_slider.setMaximumSize(QtCore.QSize(380, 16777215))
        self.contrast_slider.setSliderPosition(50)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")
        self.image_manip_layout.addWidget(self.contrast_slider, 5, 1, 1, 1)

        # add image_manip_layout to image_capture_page
        self.gridLayout_9.addLayout(self.image_manip_layout, 0, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout
        self.image_select_layout = QtWidgets.QGridLayout()
        self.image_select_layout.setObjectName("image_select_layout")

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\select_image_label
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

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\select_qr_button
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

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\qr_path_label
        self.qr_path_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qr_path_label.sizePolicy().hasHeightForWidth())
        self.qr_path_label.setSizePolicy(sizePolicy)
        self.qr_path_label.setMinimumSize(QtCore.QSize(150, 0))
        self.qr_path_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.qr_path_label.setObjectName("qr_path_label")
        self.image_select_layout.addWidget(self.qr_path_label, 1, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\qr_path
        self.qr_path = QtWidgets.QLabel(self)
        self.qr_path.setObjectName("qr_path")
        self.image_select_layout.addWidget(self.qr_path, 1, 2, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\select_barcode_button
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

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\barcode_path_label
        self.barcode_path_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_path_label.sizePolicy().hasHeightForWidth())
        self.barcode_path_label.setSizePolicy(sizePolicy)
        self.barcode_path_label.setMinimumSize(QtCore.QSize(150, 0))
        self.barcode_path_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.barcode_path_label.setObjectName("barcode_path_label")
        self.image_select_layout.addWidget(self.barcode_path_label, 2, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\barcode_path
        self.barcode_path = QtWidgets.QLabel(self)
        self.barcode_path.setObjectName("barcode_path")
        self.image_select_layout.addWidget(self.barcode_path, 2, 2, 1, 1)

        # add image_select_layout to image_capture_page and translate page
        self.gridLayout_9.addLayout(self.image_select_layout, 1, 0, 1, 1)
        self.translatePage()

        # link 'select image buttons'
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
        self.zoom_label.setText(_translate("MainWindow", "Zoom"))
        self.brightness_label.setText(_translate("MainWindow", "Brightness"))
        self.contrast_label.setText(_translate("MainWindow", "Contrast"))
        self.select_image_label.setText(_translate("MainWindow", "o  Select Images for Detection"))
        self.select_qr_button.setText(_translate("MainWindow", "Select Image (QR Code)"))
        self.qr_path_label.setText(_translate("MainWindow", "Image Path (QR Code):"))
        self.qr_path.setText(_translate("MainWindow", "No Image Selected!"))
        self.select_barcode_button.setText(_translate("MainWindow", "Select Image (Barcode)"))
        self.barcode_path_label.setText(_translate("MainWindow", "Image Path (Barcode):"))
        self.barcode_path.setText(_translate("MainWindow", "No Image Selected!"))
