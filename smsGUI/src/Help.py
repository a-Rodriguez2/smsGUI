from PyQt5 import QtCore, QtGui, QtWidgets



class HelpWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HelpWidget, self).__init__(parent)

        # help_page
        self.setObjectName("help_page")

        # help_page_layout
        self.help_page_layout = QtWidgets.QGridLayout(self)
        self.help_page_layout.setObjectName("help_page_layout")

        # help_page_layout\help_label
        self.help_label = QtWidgets.QLabel(self)
        self.help_label.setAlignment(QtCore.Qt.AlignCenter)
        self.help_label.setObjectName("help_label")
        self.help_page_layout.addWidget(self.help_label, 0, 0, 1, 1)

        # translate help_page
        self.translatePage()

    def translatePage(self):
        _translate = QtCore.QCoreApplication.translate
        self.help_label.setText(_translate("MainWindow", "HELP LABEL"))
