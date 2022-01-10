# Importing Header Files
from PyQt5 import QtCore, QtGui, QtWidgets
from Dp_popup import Ui_DisplayProfile
from post_uploader import Ui_Upload

# Main Class
class Ui_Instagram_app(object):
    # dppop will called when Dp downloader button will called
    def dppop(self):
        '''This Fnction will Launched to Display Downloader window'''
        self.window = QtWidgets.QWidget()
        self.ui = Ui_DisplayProfile()
        self. ui.setupUi(self.window)
        self.window.show()

    def postup(self):
        '''This Function will Launched to display login window and
            to upload hoto in profile'''
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Upload()
        self. ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, Instagram_app):
        Instagram_app.setObjectName("Instagram_app")
        Instagram_app.resize(368, 308)
        Instagram_app.setAutoFillBackground(False)
        Instagram_app.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(95, 42, 255, 255), stop:0.495 rgba(127, 42, 255, 255), stop:0.505 rgba(190, 23, 255, 255), stop:1 rgba(255, 74, 225, 255));\n"
"")
        # Creating Layout for Better View
        self.centralwidget = QtWidgets.QWidget(Instagram_app)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 341, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Horizental_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Horizental_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.Horizental_layout.setContentsMargins(0, 0, 0, 0)
        self.Horizental_layout.setSpacing(6)
        self.Horizental_layout.setObjectName("Horizental_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Horizental_layout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Top Lable of Main Screen
        self.Top_Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Top_Label.setFont(font)
        self.Top_Label.setStyleSheet("color: rgb(255, 26, 10);\n"
"font: 75 24pt \"Segoe UI\";\n"
"background-color: rgb(95, 42, 255);")
        self.Top_Label.setTextFormat(QtCore.Qt.RichText)
        self.Top_Label.setScaledContents(False)
        self.Top_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Top_Label.setObjectName("Top_Label")
        self.verticalLayout_2.addWidget(self.Top_Label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        # Display Downloader button Lable
        self.DP_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DP_label.setFont(font)
        self.DP_label.setStyleSheet("color: rgb(243, 255, 7);\n"
"background-color: rgb(127, 42, 255);")
        self.DP_label.setTextFormat(QtCore.Qt.RichText)
        self.DP_label.setObjectName("DP_label")
        self.verticalLayout_2.addWidget(self.DP_label)

        # Push Button which will call Dp Donloader window
        self.dp_download = QtWidgets.QPushButton(self.horizontalLayoutWidget , clicked = lambda : self.dppop())
        self.dp_download.setEnabled(True)
        self.dp_download.setAutoFillBackground(False)
        self.dp_download.setStyleSheet("background-color: rgb(127, 42, 255);\n"
"color: rgb(255, 16, 244);")
        self.dp_download.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dp_download.setCheckable(False)
        self.dp_download.setAutoDefault(True)
        self.dp_download.setDefault(False)
        self.dp_download.setFlat(False)
        self.dp_download.setObjectName("dp_download")
        self.verticalLayout_2.addWidget(self.dp_download)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        # Login Pushbutton Label
        self.login_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(221, 255, 67);\n"
"background-color: rgb(190, 23, 255);")
        self.login_label.setObjectName("login_label")
        self.verticalLayout_2.addWidget(self.login_label)
        # Login Push button
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda : self.postup())
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 74, 225);\n"
"color: rgb(103, 15, 255);\n"
"font: 75 8pt \"Tahoma\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.Horizental_layout.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Horizental_layout.addItem(spacerItem4)
        Instagram_app.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Instagram_app)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName("menubar")
        Instagram_app.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Instagram_app)
        self.statusbar.setObjectName("statusbar")
        Instagram_app.setStatusBar(self.statusbar)

        self.retranslateUi(Instagram_app)
        QtCore.QMetaObject.connectSlotsByName(Instagram_app)

    def retranslateUi(self, Instagram_app):
        # Naming All wedgits 
        _translate = QtCore.QCoreApplication.translate
        Instagram_app.setWindowTitle(_translate("Instagram_app", "MainWindow"))
        self.Top_Label.setText(_translate("Instagram_app", "Instagram Dealer"))
        self.DP_label.setText(_translate("Instagram_app", "For Dp Downloading :"))
        self.dp_download.setText(_translate("Instagram_app", "DP Download"))
        self.login_label.setText(_translate("Instagram_app", "For Uploading Post :"))
        self.pushButton_2.setText(_translate("Instagram_app", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Instagram_app = QtWidgets.QMainWindow()
    ui = Ui_Instagram_app()
    ui.setupUi(Instagram_app)
    Instagram_app.show()
    sys.exit(app.exec_())

