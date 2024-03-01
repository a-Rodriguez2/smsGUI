from PyQt5 import QtCore, QtGui, QtWidgets



class HelpWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HelpWidget, self).__init__(parent)

        # Set object name for the widget
        self.setObjectName("help_page")

        # build help label (FOR PURPOSE OF IDENTIFYING DIFFERENT WINDOWS)
        self.help_label = QtWidgets.QLabel(self)
        self.help_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.help_label.setFont(font)
        self.help_label.setAlignment(QtCore.Qt.AlignCenter)
        self.help_label.setObjectName("help_label")
        _translate = QtCore.QCoreApplication.translate
        self.help_label.setText(_translate("MainWindow", "HELP PAGE"))
