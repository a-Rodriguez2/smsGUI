from PyQt5 import QtCore, QtGui, QtWidgets



class HelpWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HelpWidget, self).__init__(parent)

        self.setObjectName("help_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # MainWindow\centralwidget\stackedWidget\help_page\help_label
        self.help_label = QtWidgets.QLabel(self)
        self.help_label.setAlignment(QtCore.Qt.AlignCenter)
        self.help_label.setObjectName("help_label")
        self.gridLayout_3.addWidget(self.help_label, 0, 0, 1, 1)

        self.translatePage()

    def translatePage(self):
        _translate = QtCore.QCoreApplication.translate
        self.help_label.setText(_translate("MainWindow", "HELP LABEL"))
