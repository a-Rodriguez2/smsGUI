from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel
from fsspec.utils import _translate


class ImageCaptureWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageCaptureWidget, self).__init__(parent)

        # Set object name for the widget
        self.setObjectName("image_capture_page")

        # Build image capture label (for the purpose of identifying different windows)
        self.image_capture_label = QtWidgets.QLabel(self)
        self.image_capture_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.image_capture_label.setFont(font)
        self.image_capture_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_capture_label.setObjectName("image_capture_label")
        _translate = QtCore.QCoreApplication.translate
        self.image_capture_label.setText(_translate("MainWindow", "IMAGE CAPTURE PAGE"))