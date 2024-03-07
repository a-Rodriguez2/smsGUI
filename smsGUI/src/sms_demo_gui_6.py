from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.image_capture_page = QtWidgets.QWidget()
        self.image_capture_page.setObjectName("image_capture_page")

        # image_capture_page layout
        self.gridLayout_9 = QtWidgets.QGridLayout(self.image_capture_page)
        self.gridLayout_9.setObjectName("gridLayout_9")

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout
        self.camera_layout = QtWidgets.QGridLayout()
        self.camera_layout.setObjectName("camera_layout")

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\save_as_button
        self.save_as_button = QtWidgets.QRadioButton(self.image_capture_page)
        self.save_as_button.setObjectName("save_as_button")
        self.camera_layout.addWidget(self.save_as_button, 3, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\save_button
        self.save_button = QtWidgets.QRadioButton(self.image_capture_page)
        self.save_button.setChecked(True)
        self.save_button.setObjectName("save_button")
        self.camera_layout.addWidget(self.save_button, 2, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\camera_layout\camera_feed_label
        self.camera_feed_label = QtWidgets.QLabel(self.image_capture_page)
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
        self.capture_image_button = QtWidgets.QPushButton(self.image_capture_page)
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
        self.video_frame = QtWidgets.QFrame(self.image_capture_page)
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
        self.zoom_label = QtWidgets.QLabel(self.image_capture_page)
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
        self.zoom_slider = QtWidgets.QSlider(self.image_capture_page)
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
        self.brightness_label = QtWidgets.QLabel(self.image_capture_page)
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
        self.brightness_slider = QtWidgets.QSlider(self.image_capture_page)
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
        self.contrast_label = QtWidgets.QLabel(self.image_capture_page)
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
        self.contrast_slider = QtWidgets.QSlider(self.image_capture_page)
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
        self.select_image_label = QtWidgets.QLabel(self.image_capture_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_image_label.sizePolicy().hasHeightForWidth())
        self.select_image_label.setSizePolicy(sizePolicy)
        self.select_image_label.setMinimumSize(QtCore.QSize(0, 60))
        self.select_image_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.select_image_label.setObjectName("select_image_label")
        self.image_select_layout.addWidget(self.select_image_label, 0, 0, 1, 2)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\proceed_button
        self.proceed_button = QtWidgets.QPushButton(self.image_capture_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceed_button.sizePolicy().hasHeightForWidth())
        self.proceed_button.setSizePolicy(sizePolicy)
        self.proceed_button.setMinimumSize(QtCore.QSize(141, 40))
        self.proceed_button.setMaximumSize(QtCore.QSize(141, 40))
        self.proceed_button.setObjectName("proceed_button")
        self.image_select_layout.addWidget(self.proceed_button, 0, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\select_qr_button
        self.select_qr_button = QtWidgets.QPushButton(self.image_capture_page)
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
        self.qr_path_label = QtWidgets.QLabel(self.image_capture_page)
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
        self.qr_path = QtWidgets.QLabel(self.image_capture_page)
        self.qr_path.setObjectName("qr_path")
        self.image_select_layout.addWidget(self.qr_path, 1, 2, 1, 1)

        # MainWindow\centralwidget\stackedWidget\image_capture_page\image_select_layout\select_barcode_button
        self.select_barcode_button = QtWidgets.QPushButton(self.image_capture_page)
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
        self.barcode_path_label = QtWidgets.QLabel(self.image_capture_page)
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
        self.barcode_path = QtWidgets.QLabel(self.image_capture_page)
        self.barcode_path.setObjectName("barcode_path")
        self.image_select_layout.addWidget(self.barcode_path, 2, 2, 1, 1)

        # add image_select_layout to image_capture_page
        self.gridLayout_9.addLayout(self.image_select_layout, 1, 0, 1, 1)

        # add image_capture_page to stackedWidget
        self.stackedWidget.addWidget(self.image_capture_page)

        # MainWindow\centralwidget\stackedWidget\detection_page (includes layout)
        self.detection_page = QtWidgets.QWidget()
        self.detection_page.setObjectName("detection_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.detection_page)
        self.gridLayout_7.setObjectName("gridLayout_7")

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts
        self.detection_prompts = QtWidgets.QGridLayout()
        self.detection_prompts.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.detection_prompts.setObjectName("detection_prompts")

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\data_matrix_label
        self.data_matrix_label = QtWidgets.QLabel(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_matrix_label.sizePolicy().hasHeightForWidth())
        self.data_matrix_label.setSizePolicy(sizePolicy)
        self.data_matrix_label.setMinimumSize(QtCore.QSize(0, 40))
        self.data_matrix_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.data_matrix_label.setObjectName("data_matrix_label")
        self.detection_prompts.addWidget(self.data_matrix_label, 0, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\matrix_recognition_button
        self.matrix_recognition_button = QtWidgets.QPushButton(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrix_recognition_button.sizePolicy().hasHeightForWidth())
        self.matrix_recognition_button.setSizePolicy(sizePolicy)
        self.matrix_recognition_button.setMinimumSize(QtCore.QSize(170, 40))
        self.matrix_recognition_button.setMaximumSize(QtCore.QSize(170, 40))
        self.matrix_recognition_button.setObjectName("matrix_recognition_button")
        self.detection_prompts.addWidget(self.matrix_recognition_button, 1, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\barcode_recognition_button
        self.barcode_recognition_button = QtWidgets.QPushButton(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_recognition_button.sizePolicy().hasHeightForWidth())
        self.barcode_recognition_button.setSizePolicy(sizePolicy)
        self.barcode_recognition_button.setMinimumSize(QtCore.QSize(170, 40))
        self.barcode_recognition_button.setMaximumSize(QtCore.QSize(170, 40))
        self.barcode_recognition_button.setObjectName("barcode_recognition_button")
        self.detection_prompts.addWidget(self.barcode_recognition_button, 1, 1, 1, 2)

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\manual_ppid_label
        self.manual_ppid_label = QtWidgets.QLabel(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_ppid_label.sizePolicy().hasHeightForWidth())
        self.manual_ppid_label.setSizePolicy(sizePolicy)
        self.manual_ppid_label.setMinimumSize(QtCore.QSize(0, 40))
        self.manual_ppid_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.manual_ppid_label.setObjectName("manual_ppid_label")
        self.detection_prompts.addWidget(self.manual_ppid_label, 2, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\ppid_user_edit
        self.ppid_user_edit = QtWidgets.QLineEdit(self.detection_page)
        self.ppid_user_edit.setObjectName("ppid_user_edit")
        self.detection_prompts.addWidget(self.ppid_user_edit, 3, 0, 1, 2)

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\ppid_user_save
        self.ppid_user_save = QtWidgets.QPushButton(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ppid_user_save.sizePolicy().hasHeightForWidth())
        self.ppid_user_save.setSizePolicy(sizePolicy)
        self.ppid_user_save.setMinimumSize(QtCore.QSize(50, 30))
        self.ppid_user_save.setMaximumSize(QtCore.QSize(50, 30))
        self.ppid_user_save.setObjectName("ppid_user_save")
        self.detection_prompts.addWidget(self.ppid_user_save, 3, 2, 1, 1)

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\image_compare_label
        self.image_compare_label = QtWidgets.QLabel(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_compare_label.sizePolicy().hasHeightForWidth())
        self.image_compare_label.setSizePolicy(sizePolicy)
        self.image_compare_label.setMinimumSize(QtCore.QSize(0, 40))
        self.image_compare_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.image_compare_label.setObjectName("image_compare_label")
        self.detection_prompts.addWidget(self.image_compare_label, 4, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\detection_page\detection_prompts\run_comparison_button
        self.run_comparison_button = QtWidgets.QPushButton(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_comparison_button.sizePolicy().hasHeightForWidth())
        self.run_comparison_button.setSizePolicy(sizePolicy)
        self.run_comparison_button.setMinimumSize(QtCore.QSize(131, 40))
        self.run_comparison_button.setMaximumSize(QtCore.QSize(131, 40))
        self.run_comparison_button.setObjectName("run_comparison_button")
        self.detection_prompts.addWidget(self.run_comparison_button, 5, 0, 1, 1)

        # add detection_prompts to detection_page
        self.gridLayout_7.addLayout(self.detection_prompts, 0, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout
        self.comparison_chosen_layout = QtWidgets.QVBoxLayout()
        self.comparison_chosen_layout.setObjectName("comparison_chosen_layout")

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\result_mobo_label
        self.result_mobo_label = QtWidgets.QLabel(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_mobo_label.sizePolicy().hasHeightForWidth())
        self.result_mobo_label.setSizePolicy(sizePolicy)
        self.result_mobo_label.setMinimumSize(QtCore.QSize(0, 20))
        self.result_mobo_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.result_mobo_label.setObjectName("result_mobo_label")
        self.comparison_chosen_layout.addWidget(self.result_mobo_label)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\result_image_frame (includes layout)
        self.result_image_frame = QtWidgets.QFrame(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_image_frame.sizePolicy().hasHeightForWidth())
        self.result_image_frame.setSizePolicy(sizePolicy)
        self.result_image_frame.setMinimumSize(QtCore.QSize(477, 268))
        self.result_image_frame.setMaximumSize(QtCore.QSize(477, 268))
        self.result_image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_image_frame.setObjectName("result_image_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.result_image_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\result_image_frame\result_image_label
        self.result_image_label = QtWidgets.QLabel(self.result_image_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_image_label.sizePolicy().hasHeightForWidth())
        self.result_image_label.setSizePolicy(sizePolicy)
        self.result_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_image_label.setObjectName("result_image_label")
        self.gridLayout_4.addWidget(self.result_image_label, 0, 0, 1, 1)

        # add result_image_frame to comparison_chosen_layout
        self.comparison_chosen_layout.addWidget(self.result_image_frame)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\open_chosen_mobo
        self.open_chosen_mobo = QtWidgets.QPushButton(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_chosen_mobo.sizePolicy().hasHeightForWidth())
        self.open_chosen_mobo.setSizePolicy(sizePolicy)
        self.open_chosen_mobo.setMinimumSize(QtCore.QSize(120, 30))
        self.open_chosen_mobo.setMaximumSize(QtCore.QSize(120, 30))
        self.open_chosen_mobo.setObjectName("open_chosen_mobo")
        self.comparison_chosen_layout.addWidget(self.open_chosen_mobo)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\chosen_mobo_label
        self.chosen_mobo_label = QtWidgets.QLabel(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chosen_mobo_label.sizePolicy().hasHeightForWidth())
        self.chosen_mobo_label.setSizePolicy(sizePolicy)
        self.chosen_mobo_label.setMinimumSize(QtCore.QSize(0, 20))
        self.chosen_mobo_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.chosen_mobo_label.setObjectName("chosen_mobo_label")
        self.comparison_chosen_layout.addWidget(self.chosen_mobo_label)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\chosen_image_frame (includes layout)
        self.chosen_image_frame = QtWidgets.QFrame(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chosen_image_frame.sizePolicy().hasHeightForWidth())
        self.chosen_image_frame.setSizePolicy(sizePolicy)
        self.chosen_image_frame.setMinimumSize(QtCore.QSize(477, 268))
        self.chosen_image_frame.setMaximumSize(QtCore.QSize(477, 268))
        self.chosen_image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chosen_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chosen_image_frame.setObjectName("chosen_image_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.chosen_image_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\chosen_image_frame\chosen_image_label
        self.chosen_image_label = QtWidgets.QLabel(self.chosen_image_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chosen_image_label.sizePolicy().hasHeightForWidth())
        self.chosen_image_label.setSizePolicy(sizePolicy)
        self.chosen_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_image_label.setObjectName("chosen_image_label")
        self.gridLayout_6.addWidget(self.chosen_image_label, 0, 0, 1, 1)

        # add chosen_image_frame to comparison_chosen_layout
        self.comparison_chosen_layout.addWidget(self.chosen_image_frame)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\open_result_mobo
        self.open_result_mobo = QtWidgets.QPushButton(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_result_mobo.sizePolicy().hasHeightForWidth())
        self.open_result_mobo.setSizePolicy(sizePolicy)
        self.open_result_mobo.setMinimumSize(QtCore.QSize(120, 30))
        self.open_result_mobo.setMaximumSize(QtCore.QSize(120, 30))
        self.open_result_mobo.setObjectName("open_result_mobo")
        self.comparison_chosen_layout.addWidget(self.open_result_mobo)

        # add comparison_chosen_layout to detection_page
        self.gridLayout_7.addLayout(self.comparison_chosen_layout, 0, 1, 2, 1)

        # MainWindow\centralwidget\stackedWidget\detection_page\reference_layout
        self.reference_layout = QtWidgets.QVBoxLayout()
        self.reference_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.reference_layout.setObjectName("reference_layout")

        # MainWindow\centralwidget\stackedWidget\detection_page\reference_layout\reference_mobo_label
        self.reference_mobo_label = QtWidgets.QLabel(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_mobo_label.sizePolicy().hasHeightForWidth())
        self.reference_mobo_label.setSizePolicy(sizePolicy)
        self.reference_mobo_label.setMinimumSize(QtCore.QSize(0, 20))
        self.reference_mobo_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.reference_mobo_label.setObjectName("reference_mobo_label")
        self.reference_layout.addWidget(self.reference_mobo_label)

        # MainWindow\centralwidget\stackedWidget\detection_page\reference_layout\reference_image_frame (includes layout)
        self.reference_image_frame = QtWidgets.QFrame(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_image_frame.sizePolicy().hasHeightForWidth())
        self.reference_image_frame.setSizePolicy(sizePolicy)
        self.reference_image_frame.setMinimumSize(QtCore.QSize(477, 268))
        self.reference_image_frame.setMaximumSize(QtCore.QSize(477, 268))
        self.reference_image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reference_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reference_image_frame.setObjectName("reference_image_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.reference_image_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")

        # MainWindow\centralwidget\stackedWidget\detection_page\reference_layout\reference_image_frame\reference_image_label
        self.reference_image_label = QtWidgets.QLabel(self.reference_image_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_image_label.sizePolicy().hasHeightForWidth())
        self.reference_image_label.setSizePolicy(sizePolicy)
        self.reference_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reference_image_label.setObjectName("reference_image_label")
        self.gridLayout_5.addWidget(self.reference_image_label, 0, 0, 1, 1)

        # add reference_image_frame to reference_layout
        self.reference_layout.addWidget(self.reference_image_frame)

        # MainWindow\centralwidget\stackedWidget\detection_page\reference_layout\open_reference_mobo
        self.open_reference_mobo = QtWidgets.QPushButton(self.detection_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_reference_mobo.sizePolicy().hasHeightForWidth())
        self.open_reference_mobo.setSizePolicy(sizePolicy)
        self.open_reference_mobo.setMinimumSize(QtCore.QSize(120, 30))
        self.open_reference_mobo.setMaximumSize(QtCore.QSize(120, 30))
        self.open_reference_mobo.setObjectName("open_reference_mobo")
        self.reference_layout.addWidget(self.open_reference_mobo)

        # add reference_layout to detection_page
        self.gridLayout_7.addLayout(self.reference_layout, 1, 0, 1, 1)

        # add detection_page to stackedWidget
        self.stackedWidget.addWidget(self.detection_page)

        # MainWindow\centralwidget\stackedWidget\generate_report_page (includes layout)
        self.generate_report_page = QtWidgets.QWidget()
        self.generate_report_page.setObjectName("generate_report_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.generate_report_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout
        self.information_layout = QtWidgets.QGridLayout()
        self.information_layout.setObjectName("information_layout")
        self.name_result = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_result.sizePolicy().hasHeightForWidth())

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\name_result
        self.name_result.setSizePolicy(sizePolicy)
        self.name_result.setMinimumSize(QtCore.QSize(100, 30))
        self.name_result.setMaximumSize(QtCore.QSize(100, 30))
        self.name_result.setObjectName("name_result")
        self.information_layout.addWidget(self.name_result, 1, 4, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\work_id_label_2
        self.work_id_label_2 = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_label_2.sizePolicy().hasHeightForWidth())
        self.work_id_label_2.setSizePolicy(sizePolicy)
        self.work_id_label_2.setMinimumSize(QtCore.QSize(60, 30))
        self.work_id_label_2.setMaximumSize(QtCore.QSize(60, 30))
        self.work_id_label_2.setObjectName("work_id_label_2")
        self.information_layout.addWidget(self.work_id_label_2, 2, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\saved_info_label_2
        self.saved_info_label_2 = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saved_info_label_2.sizePolicy().hasHeightForWidth())
        self.saved_info_label_2.setSizePolicy(sizePolicy)
        self.saved_info_label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.saved_info_label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.saved_info_label_2.setObjectName("saved_info_label_2")
        self.information_layout.addWidget(self.saved_info_label_2, 0, 3, 1, 2)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\station_number_label_2
        self.station_number_label_2 = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_number_label_2.sizePolicy().hasHeightForWidth())
        self.station_number_label_2.setSizePolicy(sizePolicy)
        self.station_number_label_2.setMinimumSize(QtCore.QSize(110, 30))
        self.station_number_label_2.setMaximumSize(QtCore.QSize(110, 30))
        self.station_number_label_2.setObjectName("station_number_label_2")
        self.information_layout.addWidget(self.station_number_label_2, 3, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\machine_name_result
        self.machine_name_result = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_name_result.sizePolicy().hasHeightForWidth())
        self.machine_name_result.setSizePolicy(sizePolicy)
        self.machine_name_result.setMinimumSize(QtCore.QSize(100, 30))
        self.machine_name_result.setMaximumSize(QtCore.QSize(100, 30))
        self.machine_name_result.setObjectName("machine_name_result")
        self.information_layout.addWidget(self.machine_name_result, 5, 4, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\refresh_button
        self.refresh_button = QtWidgets.QPushButton(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy)
        self.refresh_button.setMinimumSize(QtCore.QSize(50, 30))
        self.refresh_button.setMaximumSize(QtCore.QSize(50, 30))
        self.refresh_button.setObjectName("refresh_button")
        self.information_layout.addWidget(self.refresh_button, 6, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\work_id_result
        self.work_id_result = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_result.sizePolicy().hasHeightForWidth())
        self.work_id_result.setSizePolicy(sizePolicy)
        self.work_id_result.setMinimumSize(QtCore.QSize(100, 30))
        self.work_id_result.setMaximumSize(QtCore.QSize(100, 30))
        self.work_id_result.setObjectName("work_id_result")
        self.information_layout.addWidget(self.work_id_result, 2, 4, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\host_username_result
        self.host_username_result = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.host_username_result.sizePolicy().hasHeightForWidth())
        self.host_username_result.setSizePolicy(sizePolicy)
        self.host_username_result.setMinimumSize(QtCore.QSize(100, 30))
        self.host_username_result.setMaximumSize(QtCore.QSize(100, 30))
        self.host_username_result.setObjectName("host_username_result")
        self.information_layout.addWidget(self.host_username_result, 4, 4, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\name_label_2
        self.name_label_2 = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label_2.sizePolicy().hasHeightForWidth())
        self.name_label_2.setSizePolicy(sizePolicy)
        self.name_label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.name_label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.name_label_2.setObjectName("name_label_2")
        self.information_layout.addWidget(self.name_label_2, 1, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\host_username_label
        self.host_username_label = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.host_username_label.sizePolicy().hasHeightForWidth())
        self.host_username_label.setSizePolicy(sizePolicy)
        self.host_username_label.setMinimumSize(QtCore.QSize(110, 30))
        self.host_username_label.setMaximumSize(QtCore.QSize(110, 30))
        self.host_username_label.setObjectName("host_username_label")
        self.information_layout.addWidget(self.host_username_label, 4, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\station_number_result
        self.station_number_result = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_number_result.sizePolicy().hasHeightForWidth())
        self.station_number_result.setSizePolicy(sizePolicy)
        self.station_number_result.setMinimumSize(QtCore.QSize(100, 30))
        self.station_number_result.setMaximumSize(QtCore.QSize(100, 30))
        self.station_number_result.setObjectName("station_number_result")
        self.information_layout.addWidget(self.station_number_result, 3, 4, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\machine_name_label
        self.machine_name_label = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_name_label.sizePolicy().hasHeightForWidth())
        self.machine_name_label.setSizePolicy(sizePolicy)
        self.machine_name_label.setMinimumSize(QtCore.QSize(110, 30))
        self.machine_name_label.setMaximumSize(QtCore.QSize(110, 30))
        self.machine_name_label.setObjectName("machine_name_label")
        self.information_layout.addWidget(self.machine_name_label, 5, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\update_button
        self.update_button = QtWidgets.QPushButton(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMinimumSize(QtCore.QSize(50, 30))
        self.update_button.setMaximumSize(QtCore.QSize(50, 30))
        self.update_button.setObjectName("update_button")
        self.information_layout.addWidget(self.update_button, 4, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\work_id_label
        self.work_id_label = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_label.sizePolicy().hasHeightForWidth())
        self.work_id_label.setSizePolicy(sizePolicy)
        self.work_id_label.setMinimumSize(QtCore.QSize(60, 30))
        self.work_id_label.setMaximumSize(QtCore.QSize(60, 30))
        self.work_id_label.setObjectName("work_id_label")
        self.information_layout.addWidget(self.work_id_label, 2, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\gen_info_label
        self.gen_info_label = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_info_label.sizePolicy().hasHeightForWidth())
        self.gen_info_label.setSizePolicy(sizePolicy)
        self.gen_info_label.setMinimumSize(QtCore.QSize(0, 30))
        self.gen_info_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.gen_info_label.setObjectName("gen_info_label")
        self.information_layout.addWidget(self.gen_info_label, 0, 0, 1, 2)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\station_edit
        self.station_edit = QtWidgets.QLineEdit(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_edit.sizePolicy().hasHeightForWidth())
        self.station_edit.setSizePolicy(sizePolicy)
        self.station_edit.setObjectName("station_edit")
        self.information_layout.addWidget(self.station_edit, 3, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\name_label
        self.name_label = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setMinimumSize(QtCore.QSize(50, 30))
        self.name_label.setMaximumSize(QtCore.QSize(50, 30))
        self.name_label.setObjectName("name_label")
        self.information_layout.addWidget(self.name_label, 1, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\name_edit
        self.name_edit = QtWidgets.QLineEdit(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy)
        self.name_edit.setObjectName("name_edit")
        self.information_layout.addWidget(self.name_edit, 1, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\work_id_edit
        self.work_id_edit = QtWidgets.QLineEdit(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_edit.sizePolicy().hasHeightForWidth())
        self.work_id_edit.setSizePolicy(sizePolicy)
        self.work_id_edit.setObjectName("work_id_edit")
        self.information_layout.addWidget(self.work_id_edit, 2, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\station_number_label
        self.station_number_label = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_number_label.sizePolicy().hasHeightForWidth())
        self.station_number_label.setSizePolicy(sizePolicy)
        self.station_number_label.setMinimumSize(QtCore.QSize(110, 30))
        self.station_number_label.setMaximumSize(QtCore.QSize(110, 30))
        self.station_number_label.setObjectName("station_number_label")
        self.information_layout.addWidget(self.station_number_label, 3, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\information_spacer
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.information_layout.addItem(spacerItem4, 2, 2, 1, 1)

        # add information_layout to generate_report_page
        self.verticalLayout_2.addLayout(self.information_layout)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\generate_report_layout
        self.generate_report_layout = QtWidgets.QGridLayout()
        self.generate_report_layout.setObjectName("generate_report_layout")

        # MainWindow\centralwidget\stackedWidget\generate_report_page\generate_report_layout\preview_report_button
        self.preview_report_button = QtWidgets.QPushButton(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_report_button.sizePolicy().hasHeightForWidth())
        self.preview_report_button.setSizePolicy(sizePolicy)
        self.preview_report_button.setMinimumSize(QtCore.QSize(131, 40))
        self.preview_report_button.setMaximumSize(QtCore.QSize(131, 40))
        self.preview_report_button.setObjectName("preview_report_button")
        self.generate_report_layout.addWidget(self.preview_report_button, 1, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\generate_report_layout\generate_report_label
        self.generate_report_label = QtWidgets.QLabel(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_report_label.sizePolicy().hasHeightForWidth())
        self.generate_report_label.setSizePolicy(sizePolicy)
        self.generate_report_label.setMinimumSize(QtCore.QSize(0, 30))
        self.generate_report_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.generate_report_label.setObjectName("generate_report_label")
        self.generate_report_layout.addWidget(self.generate_report_label, 0, 0, 1, 2)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\generate_report_layout\generate_report_button_2
        self.generate_report_button_2 = QtWidgets.QPushButton(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_report_button_2.sizePolicy().hasHeightForWidth())
        self.generate_report_button_2.setSizePolicy(sizePolicy)
        self.generate_report_button_2.setMinimumSize(QtCore.QSize(131, 40))
        self.generate_report_button_2.setMaximumSize(QtCore.QSize(131, 40))
        self.generate_report_button_2.setObjectName("generate_report_button_2")
        self.generate_report_layout.addWidget(self.generate_report_button_2, 2, 0, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\generate_report_layout\save_radio_button
        self.save_radio_button = QtWidgets.QRadioButton(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_radio_button.sizePolicy().hasHeightForWidth())
        self.save_radio_button.setSizePolicy(sizePolicy)
        self.save_radio_button.setChecked(True)
        self.save_radio_button.setObjectName("save_radio_button")
        self.generate_report_layout.addWidget(self.save_radio_button, 1, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\generate_report_layout\save_as_radio_button
        self.save_as_radio_button = QtWidgets.QRadioButton(self.generate_report_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as_radio_button.sizePolicy().hasHeightForWidth())
        self.save_as_radio_button.setSizePolicy(sizePolicy)
        self.save_as_radio_button.setObjectName("save_as_radio_button")
        self.generate_report_layout.addWidget(self.save_as_radio_button, 2, 1, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\generate_report_layout\generate_report_spacer
        spacerItem5 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.generate_report_layout.addItem(spacerItem5, 1, 2, 1, 1)

        # add generate_report_layout to generate_report_page
        self.verticalLayout_2.addLayout(self.generate_report_layout)

        # add generate_report_page to stackedWidget
        self.stackedWidget.addWidget(self.generate_report_page)

        # MainWindow\centralwidget\stackedWidget\help_page (includes layout)
        self.help_page = QtWidgets.QWidget()
        self.help_page.setObjectName("help_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.help_page)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # MainWindow\centralwidget\stackedWidget\help_page\help_label
        self.help_label = QtWidgets.QLabel(self.help_page)
        self.help_label.setAlignment(QtCore.Qt.AlignCenter)
        self.help_label.setObjectName("help_label")
        self.gridLayout_3.addWidget(self.help_label, 0, 0, 1, 1)

        # add help_page to stackedWidget
        self.stackedWidget.addWidget(self.help_page)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        # set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        # translate GUI
        self.retranslateUi(MainWindow)
        #set initial stackedWidget window
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connect sidebar buttons to their respective widgets within the stacked widget
        self.image_capture_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.image_capture_page))
        self.detection_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.detection_page))
        self.generate_report_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.generate_report_page))
        self.help_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.help_page))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SMS Demo Gui V5"))
        self.company_name.setText(_translate("MainWindow", "SMS InfoComm"))
        self.app_name.setText(_translate("MainWindow", "Motherboard Inspection"))
        self.image_capture_button.setText(_translate("MainWindow", "Image Capture"))
        self.detection_button.setText(_translate("MainWindow", "Detection"))
        self.generate_report_button.setText(_translate("MainWindow", "Generate Report"))
        self.help_button.setText(_translate("MainWindow", "Help!"))
        self.save_as_button.setText(_translate("MainWindow", "- Save As -"))
        self.save_button.setText(_translate("MainWindow", "- Save -  "))
        self.camera_feed_label.setText(_translate("MainWindow", "o  Camera Live Feed"))
        self.capture_image_button.setText(_translate("MainWindow", "Capture Image"))
        self.video_frame_label.setText(_translate("MainWindow", "- Video Frame -"))
        self.zoom_label.setText(_translate("MainWindow", "Zoom"))
        self.brightness_label.setText(_translate("MainWindow", "Brightness"))
        self.contrast_label.setText(_translate("MainWindow", "Contrast"))
        self.select_image_label.setText(_translate("MainWindow", "o  Select Images for Detection"))
        self.proceed_button.setText(_translate("MainWindow", "Proceed to Detection"))
        self.select_qr_button.setText(_translate("MainWindow", "Select Image (QR Code)"))
        self.qr_path_label.setText(_translate("MainWindow", "Image Path (QR Code):"))
        self.qr_path.setText(_translate("MainWindow", "No Image Selected!"))
        self.select_barcode_button.setText(_translate("MainWindow", "Select Image (Barcode)"))
        self.barcode_path_label.setText(_translate("MainWindow", "Image Path (Barcode):"))
        self.barcode_path.setText(_translate("MainWindow", "No Image Selected!"))
        self.data_matrix_label.setText(_translate("MainWindow", "o  Data Matrix and Barcode"))
        self.matrix_recognition_button.setText(_translate("MainWindow", "Run Recognition (Data Matrix)"))
        self.barcode_recognition_button.setText(_translate("MainWindow", "Run Recognition (Barcode)"))
        self.manual_ppid_label.setText(_translate("MainWindow", "o  Manually Enter PPID:"))
        self.ppid_user_save.setText(_translate("MainWindow", "Save"))
        self.image_compare_label.setText(_translate("MainWindow", "o  Image Comparison"))
        self.run_comparison_button.setText(_translate("MainWindow", "Run Comparison"))
        self.result_mobo_label.setText(_translate("MainWindow", "Comparison Result"))
        self.result_image_label.setText(_translate("MainWindow", "- Result Image Frame -"))
        self.open_chosen_mobo.setText(_translate("MainWindow", "Open File Location"))
        self.chosen_mobo_label.setText(_translate("MainWindow", "Chosen Motherboard"))
        self.chosen_image_label.setText(_translate("MainWindow", "- Chosen Image Frame -"))
        self.open_result_mobo.setText(_translate("MainWindow", "Open File Location"))
        self.reference_mobo_label.setText(_translate("MainWindow", "Reference Motherboard"))
        self.reference_image_label.setText(_translate("MainWindow", "- Reference Image Frame -"))
        self.open_reference_mobo.setText(_translate("MainWindow", "Open File Location"))
        self.name_result.setText(_translate("MainWindow", "None"))
        self.work_id_label_2.setText(_translate("MainWindow", "Work ID:"))
        self.saved_info_label_2.setText(_translate("MainWindow", "o  Saved Information"))
        self.station_number_label_2.setText(_translate("MainWindow", "Station Number:"))
        self.machine_name_result.setText(_translate("MainWindow", "None"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.work_id_result.setText(_translate("MainWindow", "None"))
        self.host_username_result.setText(_translate("MainWindow", "None"))
        self.name_label_2.setText(_translate("MainWindow", "Name:"))
        self.host_username_label.setText(_translate("MainWindow", "Host Username:"))
        self.station_number_result.setText(_translate("MainWindow", "None"))
        self.machine_name_label.setText(_translate("MainWindow", "Machine Name:"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.work_id_label.setText(_translate("MainWindow", "Work ID:"))
        self.gen_info_label.setText(_translate("MainWindow", "o  General Information"))
        self.name_label.setText(_translate("MainWindow", "Name:"))
        self.station_number_label.setText(_translate("MainWindow", "Station Number:"))
        self.preview_report_button.setText(_translate("MainWindow", "Preview Report"))
        self.generate_report_label.setText(_translate("MainWindow", "o  Generate Report"))
        self.generate_report_button_2.setText(_translate("MainWindow", "Generate Report"))
        self.save_radio_button.setText(_translate("MainWindow", "- Save -  "))
        self.save_as_radio_button.setText(_translate("MainWindow", "- Save As -"))
        self.help_label.setText(_translate("MainWindow", "HELP LABEL"))


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
