from PyQt5 import QtCore, QtGui, QtWidgets



class DetectionWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DetectionWidget, self).__init__(parent)

        self.setObjectName("detection_page")

        # build detection label (FOR PURPOSE OF IDENTIFYING DIFFERENT WINDOWS)
        self.detection_label = QtWidgets.QLabel(self)
        self.detection_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.detection_label.setFont(font)
        self.detection_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detection_label.setObjectName("detection_label")
        _translate = QtCore.QCoreApplication.translate
        self.detection_label.setText(_translate("MainWindow", "DETECTION PAGE"))
