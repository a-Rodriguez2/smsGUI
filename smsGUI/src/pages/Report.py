from PyQt5 import QtCore, QtGui, QtWidgets
import getpass
import socket


class ReportWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ReportWidget, self).__init__(parent)

        # generate_report_page
        self.setObjectName("generate_report_page")

        # generate_report_page_layout
        self.generate_report_page_layout = QtWidgets.QVBoxLayout(self)
        self.generate_report_page_layout.setObjectName("generate_report_page_layout")

        # information_layout
        self.information_layout = QtWidgets.QGridLayout()
        self.information_layout.setObjectName("information_layout")

        # information_layout\name_result
        self.name_result = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_result.sizePolicy().hasHeightForWidth())
        self.name_result.setSizePolicy(sizePolicy)
        self.name_result.setMinimumSize(QtCore.QSize(100, 30))
        self.name_result.setMaximumSize(QtCore.QSize(100, 30))
        self.name_result.setObjectName("name_result")
        self.information_layout.addWidget(self.name_result, 1, 4, 1, 1)

        # information_layout\work_id_label_2
        self.work_id_label_2 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_label_2.sizePolicy().hasHeightForWidth())
        self.work_id_label_2.setSizePolicy(sizePolicy)
        self.work_id_label_2.setMinimumSize(QtCore.QSize(60, 30))
        self.work_id_label_2.setMaximumSize(QtCore.QSize(60, 30))
        self.work_id_label_2.setObjectName("work_id_label_2")
        self.information_layout.addWidget(self.work_id_label_2, 2, 3, 1, 1)

        # information_layout\saved_info_label_2
        self.saved_info_label_2 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saved_info_label_2.sizePolicy().hasHeightForWidth())
        self.saved_info_label_2.setSizePolicy(sizePolicy)
        self.saved_info_label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.saved_info_label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.saved_info_label_2.setObjectName("saved_info_label_2")
        self.information_layout.addWidget(self.saved_info_label_2, 0, 3, 1, 2)

        # information_layout\station_number_label_2
        self.station_number_label_2 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_number_label_2.sizePolicy().hasHeightForWidth())
        self.station_number_label_2.setSizePolicy(sizePolicy)
        self.station_number_label_2.setMinimumSize(QtCore.QSize(110, 30))
        self.station_number_label_2.setMaximumSize(QtCore.QSize(110, 30))
        self.station_number_label_2.setObjectName("station_number_label_2")
        self.information_layout.addWidget(self.station_number_label_2, 3, 3, 1, 1)

        # information_layout\machine_name_result
        self.machine_name_result = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_name_result.sizePolicy().hasHeightForWidth())
        self.machine_name_result.setSizePolicy(sizePolicy)
        self.machine_name_result.setMinimumSize(QtCore.QSize(100, 30))
        self.machine_name_result.setMaximumSize(QtCore.QSize(100, 30))
        self.machine_name_result.setObjectName("machine_name_result")
        self.information_layout.addWidget(self.machine_name_result, 5, 4, 1, 1)

        # information_layout\update_button
        self.update_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMinimumSize(QtCore.QSize(50, 30))
        self.update_button.setMaximumSize(QtCore.QSize(50, 30))
        self.update_button.setObjectName("update_button")
        self.information_layout.addWidget(self.update_button, 4, 0, 1, 1)

        # information_layout\work_id_result
        self.work_id_result = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_result.sizePolicy().hasHeightForWidth())
        self.work_id_result.setSizePolicy(sizePolicy)
        self.work_id_result.setMinimumSize(QtCore.QSize(100, 30))
        self.work_id_result.setMaximumSize(QtCore.QSize(100, 30))
        self.work_id_result.setObjectName("work_id_result")
        self.information_layout.addWidget(self.work_id_result, 2, 4, 1, 1)

        # information_layout\system_username_result
        self.system_username_result = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_username_result.sizePolicy().hasHeightForWidth())
        self.system_username_result.setSizePolicy(sizePolicy)
        self.system_username_result.setMinimumSize(QtCore.QSize(100, 30))
        self.system_username_result.setMaximumSize(QtCore.QSize(100, 30))
        self.system_username_result.setObjectName("system_username_result")
        self.information_layout.addWidget(self.system_username_result, 4, 4, 1, 1)

        # information_layout\name_label_2
        self.name_label_2 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label_2.sizePolicy().hasHeightForWidth())
        self.name_label_2.setSizePolicy(sizePolicy)
        self.name_label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.name_label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.name_label_2.setObjectName("name_label_2")
        self.information_layout.addWidget(self.name_label_2, 1, 3, 1, 1)

        # MainWindow\centralwidget\stackedWidget\generate_report_page\information_layout\system_username_label
        self.system_username_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_username_label.sizePolicy().hasHeightForWidth())
        self.system_username_label.setSizePolicy(sizePolicy)
        self.system_username_label.setMinimumSize(QtCore.QSize(110, 30))
        self.system_username_label.setMaximumSize(QtCore.QSize(110, 30))
        self.system_username_label.setObjectName("system_username_label")
        self.information_layout.addWidget(self.system_username_label, 4, 3, 1, 1)

        # information_layout\station_number_result
        self.station_number_result = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_number_result.sizePolicy().hasHeightForWidth())
        self.station_number_result.setSizePolicy(sizePolicy)
        self.station_number_result.setMinimumSize(QtCore.QSize(100, 30))
        self.station_number_result.setMaximumSize(QtCore.QSize(100, 30))
        self.station_number_result.setObjectName("station_number_result")
        self.information_layout.addWidget(self.station_number_result, 3, 4, 1, 1)

        # information_layout\machine_name_label
        self.machine_name_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_name_label.sizePolicy().hasHeightForWidth())
        self.machine_name_label.setSizePolicy(sizePolicy)
        self.machine_name_label.setMinimumSize(QtCore.QSize(110, 30))
        self.machine_name_label.setMaximumSize(QtCore.QSize(110, 30))
        self.machine_name_label.setObjectName("machine_name_label")
        self.information_layout.addWidget(self.machine_name_label, 5, 3, 1, 1)

        # information_layout\work_id_label
        self.work_id_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_label.sizePolicy().hasHeightForWidth())
        self.work_id_label.setSizePolicy(sizePolicy)
        self.work_id_label.setMinimumSize(QtCore.QSize(60, 30))
        self.work_id_label.setMaximumSize(QtCore.QSize(60, 30))
        self.work_id_label.setObjectName("work_id_label")
        self.information_layout.addWidget(self.work_id_label, 2, 0, 1, 1)

        # information_layout\gen_info_label
        self.gen_info_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_info_label.sizePolicy().hasHeightForWidth())
        self.gen_info_label.setSizePolicy(sizePolicy)
        self.gen_info_label.setMinimumSize(QtCore.QSize(0, 30))
        self.gen_info_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.gen_info_label.setObjectName("gen_info_label")
        self.information_layout.addWidget(self.gen_info_label, 0, 0, 1, 2)

        # information_layout\station_edit
        self.station_edit = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_edit.sizePolicy().hasHeightForWidth())
        self.station_edit.setSizePolicy(sizePolicy)
        self.station_edit.setObjectName("station_edit")
        self.information_layout.addWidget(self.station_edit, 3, 1, 1, 1)

        # information_layout\name_label
        self.name_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setMinimumSize(QtCore.QSize(50, 30))
        self.name_label.setMaximumSize(QtCore.QSize(50, 30))
        self.name_label.setObjectName("name_label")
        self.information_layout.addWidget(self.name_label, 1, 0, 1, 1)

        # information_layout\name_edit
        self.name_edit = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy)
        self.name_edit.setObjectName("name_edit")
        self.information_layout.addWidget(self.name_edit, 1, 1, 1, 1)

        # information_layout\work_id_edit
        self.work_id_edit = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_id_edit.sizePolicy().hasHeightForWidth())
        self.work_id_edit.setSizePolicy(sizePolicy)
        self.work_id_edit.setObjectName("work_id_edit")
        self.information_layout.addWidget(self.work_id_edit, 2, 1, 1, 1)

        # information_layout\station_number_label
        self.station_number_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.station_number_label.sizePolicy().hasHeightForWidth())
        self.station_number_label.setSizePolicy(sizePolicy)
        self.station_number_label.setMinimumSize(QtCore.QSize(110, 30))
        self.station_number_label.setMaximumSize(QtCore.QSize(110, 30))
        self.station_number_label.setObjectName("station_number_label")
        self.information_layout.addWidget(self.station_number_label, 3, 0, 1, 1)

        # information_layout\information_spacer
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.information_layout.addItem(spacerItem4, 2, 2, 1, 1)

        # add information_layout to generate_report_page_layout
        self.generate_report_page_layout.addLayout(self.information_layout)

        # generate_report_layout
        self.generate_report_layout = QtWidgets.QGridLayout()
        self.generate_report_layout.setObjectName("generate_report_layout")

        # generate_report_layout\preview_report_button
        self.preview_report_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_report_button.sizePolicy().hasHeightForWidth())
        self.preview_report_button.setSizePolicy(sizePolicy)
        self.preview_report_button.setMinimumSize(QtCore.QSize(131, 40))
        self.preview_report_button.setMaximumSize(QtCore.QSize(131, 40))
        self.preview_report_button.setObjectName("preview_report_button")
        self.generate_report_layout.addWidget(self.preview_report_button, 1, 0, 1, 1)

        # generate_report_layout\generate_report_label
        self.generate_report_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_report_label.sizePolicy().hasHeightForWidth())
        self.generate_report_label.setSizePolicy(sizePolicy)
        self.generate_report_label.setMinimumSize(QtCore.QSize(0, 30))
        self.generate_report_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.generate_report_label.setObjectName("generate_report_label")
        self.generate_report_layout.addWidget(self.generate_report_label, 0, 0, 1, 2)

        # generate_report_layout\generate_report_button_2
        self.generate_report_button_2 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_report_button_2.sizePolicy().hasHeightForWidth())
        self.generate_report_button_2.setSizePolicy(sizePolicy)
        self.generate_report_button_2.setMinimumSize(QtCore.QSize(131, 40))
        self.generate_report_button_2.setMaximumSize(QtCore.QSize(131, 40))
        self.generate_report_button_2.setObjectName("generate_report_button_2")
        self.generate_report_layout.addWidget(self.generate_report_button_2, 2, 0, 1, 1)

        # generate_report_layout\save_radio_button
        self.save_radio_button = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_radio_button.sizePolicy().hasHeightForWidth())
        self.save_radio_button.setSizePolicy(sizePolicy)
        self.save_radio_button.setChecked(True)
        self.save_radio_button.setObjectName("save_radio_button")
        self.generate_report_layout.addWidget(self.save_radio_button, 1, 1, 1, 1)

        # generate_report_layout\save_as_radio_button
        self.save_as_radio_button = QtWidgets.QRadioButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as_radio_button.sizePolicy().hasHeightForWidth())
        self.save_as_radio_button.setSizePolicy(sizePolicy)
        self.save_as_radio_button.setObjectName("save_as_radio_button")
        self.generate_report_layout.addWidget(self.save_as_radio_button, 2, 1, 1, 1)

        # generate_report_layout\restart_program_button
        self.restart_program_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restart_program_button.sizePolicy().hasHeightForWidth())
        self.restart_program_button.setSizePolicy(sizePolicy)
        self.restart_program_button.setMinimumSize(QtCore.QSize(131, 40))
        self.restart_program_button.setObjectName("restart_program_button")
        self.generate_report_layout.addWidget(self.restart_program_button, 2, 2, 1, 1)

        # generate_report_layout\spacerItem5
        spacerItem5 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.generate_report_layout.addItem(spacerItem5, 1, 2, 1, 1)

        # add generate_report_layout to generate_report_page_layout
        self.generate_report_page_layout.addLayout(self.generate_report_layout)

        # translate generate_report_page
        self.translatePage()

        # link update_button to saved information labels
        self.update_button.clicked.connect(lambda: self.update_info())

    # update saved information based on OS/machine credentials and user-edited information
    def update_info(self):

        # update information using existing line edits
        if self.name_edit.text() != '':
            self.name_result.setText(self.name_edit.text())
        if self.work_id_edit.text() != '':
            self.work_id_result.setText(self.work_id_edit.text())
        if self.station_edit.text() != '':
            self.station_number_result.setText(self.station_edit.text())

        self.system_username_result.setText(getpass.getuser())
        self.machine_name_result.setText(socket.gethostname())

    def translatePage(self):
        _translate = QtCore.QCoreApplication.translate

        self.name_result.setText(_translate("MainWindow", "None"))
        self.work_id_label_2.setText(_translate("MainWindow", "Work ID:"))
        self.saved_info_label_2.setText(_translate("MainWindow", "o  Saved Information"))
        self.station_number_label_2.setText(_translate("MainWindow", "Station Number:"))
        self.machine_name_result.setText(_translate("MainWindow", "None"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.work_id_result.setText(_translate("MainWindow", "None"))
        self.system_username_result.setText(_translate("MainWindow", "None"))
        self.name_label_2.setText(_translate("MainWindow", "Name:"))
        self.system_username_label.setText(_translate("MainWindow", "System Username:"))
        self.station_number_result.setText(_translate("MainWindow", "None"))
        self.machine_name_label.setText(_translate("MainWindow", "Machine Name:"))
        self.work_id_label.setText(_translate("MainWindow", "Work ID:"))
        self.gen_info_label.setText(_translate("MainWindow", "o  General Information"))
        self.name_label.setText(_translate("MainWindow", "Name:"))
        self.station_number_label.setText(_translate("MainWindow", "Station Number:"))
        self.preview_report_button.setText(_translate("MainWindow", "Preview Report"))
        self.generate_report_label.setText(_translate("MainWindow", "o  Generate Report"))
        self.generate_report_button_2.setText(_translate("MainWindow", "Generate Report"))
        self.save_radio_button.setText(_translate("MainWindow", "- Save -  "))
        self.save_as_radio_button.setText(_translate("MainWindow", "- Save As -"))
        self.restart_program_button.setText(_translate("MainWindow", "Restart Program"))
