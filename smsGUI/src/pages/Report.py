from PyQt5 import QtCore, QtGui, QtWidgets



class ReportWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ReportWidget, self).__init__(parent)

        self.setObjectName("generate_report_page")

        self.report_label = QtWidgets.QLabel(self)
        self.report_label.setGeometry(QtCore.QRect(180, 140, 431, 221))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.report_label.setFont(font)
        self.report_label.setAlignment(QtCore.Qt.AlignCenter)
        self.report_label.setObjectName("report_label")
        _translate = QtCore.QCoreApplication.translate
        self.report_label.setText(_translate("MainWindow", "REPORT PAGE"))
