from PyQt5 import QtCore, QtGui, QtWidgets
from pages.ImageCapture import ImageCaptureWidget
from pages.Detection import DetectionWidget


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
