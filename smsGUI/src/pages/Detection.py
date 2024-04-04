from PyQt5 import QtCore, QtGui, QtWidgets


class DetectionWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DetectionWidget, self).__init__(parent)

        # detection page
        self.setObjectName("detection_page")

        # detection_page_layout
        self.detection_page_layout = QtWidgets.QGridLayout(self)
        self.detection_page_layout.setObjectName("detection_page_layout")

        # detection_prompts
        self.detection_prompts = QtWidgets.QGridLayout()
        self.detection_prompts.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.detection_prompts.setContentsMargins(10, 10, 10, 10)
        self.detection_prompts.setObjectName("detection_prompts")

        # detection_prompts\result_ppid_label
        self.result_ppid_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_ppid_label.sizePolicy().hasHeightForWidth())
        self.result_ppid_label.setSizePolicy(sizePolicy)
        self.result_ppid_label.setMinimumSize(QtCore.QSize(80, 30))
        self.result_ppid_label.setMaximumSize(QtCore.QSize(80, 30))
        self.result_ppid_label.setObjectName("result_ppid_label")
        self.detection_prompts.addWidget(self.result_ppid_label, 5, 0, 1, 1)

        # detection_prompts\data_matrix_label
        self.data_matrix_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_matrix_label.sizePolicy().hasHeightForWidth())
        self.data_matrix_label.setSizePolicy(sizePolicy)
        self.data_matrix_label.setMinimumSize(QtCore.QSize(0, 40))
        self.data_matrix_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.data_matrix_label.setObjectName("data_matrix_label")
        self.detection_prompts.addWidget(self.data_matrix_label, 0, 0, 1, 1)

        # detection_prompts\matrix_recognition_button
        self.matrix_recognition_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrix_recognition_button.sizePolicy().hasHeightForWidth())
        self.matrix_recognition_button.setSizePolicy(sizePolicy)
        self.matrix_recognition_button.setMinimumSize(QtCore.QSize(170, 40))
        self.matrix_recognition_button.setMaximumSize(QtCore.QSize(170, 40))
        self.matrix_recognition_button.setObjectName("matrix_recognition_button")
        self.detection_prompts.addWidget(self.matrix_recognition_button, 1, 0, 1, 1)

        # detection_prompts\barcode_recognition_button
        self.barcode_recognition_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_recognition_button.sizePolicy().hasHeightForWidth())
        self.barcode_recognition_button.setSizePolicy(sizePolicy)
        self.barcode_recognition_button.setMinimumSize(QtCore.QSize(170, 40))
        self.barcode_recognition_button.setMaximumSize(QtCore.QSize(170, 40))
        self.barcode_recognition_button.setObjectName("barcode_recognition_button")
        self.detection_prompts.addWidget(self.barcode_recognition_button, 1, 1, 1, 2)

        # detection_prompts\manual_ppid_label
        self.manual_ppid_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_ppid_label.sizePolicy().hasHeightForWidth())
        self.manual_ppid_label.setSizePolicy(sizePolicy)
        self.manual_ppid_label.setMinimumSize(QtCore.QSize(0, 40))
        self.manual_ppid_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.manual_ppid_label.setObjectName("manual_ppid_label")
        self.detection_prompts.addWidget(self.manual_ppid_label, 2, 0, 1, 1)

        # detection_prompts\ppid_user_edit
        self.ppid_user_edit = QtWidgets.QLineEdit(self)
        self.ppid_user_edit.setObjectName("ppid_user_edit")
        self.detection_prompts.addWidget(self.ppid_user_edit, 3, 0, 1, 2)

        # detection_prompts\ppid_user_save
        self.ppid_user_save = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ppid_user_save.sizePolicy().hasHeightForWidth())
        self.ppid_user_save.setSizePolicy(sizePolicy)
        self.ppid_user_save.setMinimumSize(QtCore.QSize(50, 30))
        self.ppid_user_save.setMaximumSize(QtCore.QSize(50, 30))
        self.ppid_user_save.setObjectName("ppid_user_save")
        self.detection_prompts.addWidget(self.ppid_user_save, 3, 2, 1, 1)

        # detection_prompts\image_compare_label
        self.image_compare_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_compare_label.sizePolicy().hasHeightForWidth())
        self.image_compare_label.setSizePolicy(sizePolicy)
        self.image_compare_label.setMinimumSize(QtCore.QSize(0, 40))
        self.image_compare_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.image_compare_label.setObjectName("image_compare_label")
        self.detection_prompts.addWidget(self.image_compare_label, 6, 0, 1, 1)

        # detection_prompts\run_comparison_button
        self.run_comparison_button = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_comparison_button.sizePolicy().hasHeightForWidth())
        self.run_comparison_button.setSizePolicy(sizePolicy)
        self.run_comparison_button.setMinimumSize(QtCore.QSize(131, 40))
        self.run_comparison_button.setMaximumSize(QtCore.QSize(131, 40))
        self.run_comparison_button.setObjectName("run_comparison_button")
        self.detection_prompts.addWidget(self.run_comparison_button, 7, 0, 1, 1)

        # detection_prompts\result_ppid
        self.result_ppid = QtWidgets.QLabel(self)
        self.result_ppid.setObjectName("result_ppid")
        self.detection_prompts.addWidget(self.result_ppid, 5, 1, 1, 1)

        # add detection_prompts to detection_page_layout
        self.detection_page_layout.addLayout(self.detection_prompts, 0, 0, 1, 1)

        # chosen and result layout
        self.chosen_and_result_layout = QtWidgets.QVBoxLayout()
        self.chosen_and_result_layout.setContentsMargins(10, 10, 10, 10)
        self.chosen_and_result_layout.setObjectName("chosen_and_result_layout")

        # chosen_and_result_layout\result_mobo_label
        self.result_mobo_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_mobo_label.sizePolicy().hasHeightForWidth())
        self.result_mobo_label.setSizePolicy(sizePolicy)
        self.result_mobo_label.setMinimumSize(QtCore.QSize(0, 20))
        self.result_mobo_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.result_mobo_label.setObjectName("result_mobo_label")
        self.chosen_and_result_layout.addWidget(self.result_mobo_label)

        # chosen_and_result_layout\result_image_label
        self.result_image_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_image_label.sizePolicy().hasHeightForWidth())
        self.result_image_label.setSizePolicy(sizePolicy)
        self.result_image_label.setMinimumSize(QtCore.QSize(640, 360))
        self.result_image_label.setMaximumSize(QtCore.QSize(640, 360))
        self.result_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_image_label.setObjectName("result_image_label")
        self.chosen_and_result_layout.addWidget(self.result_image_label)

        # chosen_and_result_layout\open_result_mobo
        self.open_result_mobo = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_result_mobo.sizePolicy().hasHeightForWidth())
        self.open_result_mobo.setSizePolicy(sizePolicy)
        self.open_result_mobo.setMinimumSize(QtCore.QSize(120, 30))
        self.open_result_mobo.setMaximumSize(QtCore.QSize(120, 30))
        self.open_result_mobo.setObjectName("open_chosen_mobo")
        self.chosen_and_result_layout.addWidget(self.open_result_mobo)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\chosen_mobo_label
        self.chosen_mobo_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chosen_mobo_label.sizePolicy().hasHeightForWidth())
        self.chosen_mobo_label.setSizePolicy(sizePolicy)
        self.chosen_mobo_label.setMinimumSize(QtCore.QSize(0, 20))
        self.chosen_mobo_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.chosen_mobo_label.setObjectName("chosen_mobo_label")
        self.chosen_and_result_layout.addWidget(self.chosen_mobo_label)

        # MainWindow\centralwidget\stackedWidget\detection_page\comparison_chosen_layout\chosen_image_frame\chosen_image_label
        self.chosen_image_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chosen_image_label.sizePolicy().hasHeightForWidth())
        self.chosen_image_label.setSizePolicy(sizePolicy)
        self.chosen_image_label.setMinimumSize(QtCore.QSize(640, 360))
        self.chosen_image_label.setMaximumSize(QtCore.QSize(640, 360))
        self.chosen_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_image_label.setObjectName("chosen_image_label")
        self.chosen_and_result_layout.addWidget(self.chosen_image_label)

        # chosen_and_result_layout\open_chosen_mobo
        self.open_chosen_mobo = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_chosen_mobo.sizePolicy().hasHeightForWidth())
        self.open_chosen_mobo.setSizePolicy(sizePolicy)
        self.open_chosen_mobo.setMinimumSize(QtCore.QSize(120, 30))
        self.open_chosen_mobo.setMaximumSize(QtCore.QSize(120, 30))
        self.open_chosen_mobo.setObjectName("open_result_mobo")
        self.chosen_and_result_layout.addWidget(self.open_chosen_mobo)

        # add chosen_and_result_layout to detection_page
        self.detection_page_layout.addLayout(self.chosen_and_result_layout, 0, 1, 2, 1)

        # reference_layout
        self.reference_layout = QtWidgets.QVBoxLayout()
        self.reference_layout.setContentsMargins(10, 10, 10, 10)
        self.reference_layout.setObjectName("reference_layout")

        # reference_layout\reference_mobo_label
        self.reference_mobo_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_mobo_label.sizePolicy().hasHeightForWidth())
        self.reference_mobo_label.setSizePolicy(sizePolicy)
        self.reference_mobo_label.setMinimumSize(QtCore.QSize(0, 20))
        self.reference_mobo_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.reference_mobo_label.setObjectName("reference_mobo_label")
        self.reference_layout.addWidget(self.reference_mobo_label)

        # reference_layout\reference_image_label
        self.reference_image_label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_image_label.sizePolicy().hasHeightForWidth())
        self.reference_image_label.setSizePolicy(sizePolicy)
        self.reference_image_label.setMinimumSize(QtCore.QSize(640, 360))
        self.reference_image_label.setMaximumSize(QtCore.QSize(640, 360))
        self.reference_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reference_image_label.setObjectName("reference_image_label")
        self.reference_layout.addWidget(self.reference_image_label)

        # reference_layout\open_reference_mobo
        self.open_reference_mobo = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_reference_mobo.sizePolicy().hasHeightForWidth())
        self.open_reference_mobo.setSizePolicy(sizePolicy)
        self.open_reference_mobo.setMinimumSize(QtCore.QSize(120, 30))
        self.open_reference_mobo.setMaximumSize(QtCore.QSize(120, 30))
        self.open_reference_mobo.setObjectName("open_reference_mobo")
        self.reference_layout.addWidget(self.open_reference_mobo)

        # add reference_layout to detection_page_layout
        self.detection_page_layout.addLayout(self.reference_layout, 1, 0, 1, 1)

        # initially disable 'open file location' buttons until

        # translate detection_page
        self.translatePage()

    def translatePage(self):
        _translate = QtCore.QCoreApplication.translate
        self.data_matrix_label.setText(_translate("MainWindow", "o  QR Code and Barcode Recognition"))
        self.matrix_recognition_button.setText(_translate("MainWindow", "Run Recognition (QR Code)"))
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
        self.result_ppid.setText(_translate("MainWindow", "None"))
        self.result_ppid_label.setText(_translate("MainWindow", "Result PPID:"))
