from PyQt5 import QtCore, QtGui, QtWidgets
import instaloader

class Ui_DisplayProfile(object):
        
    def setupUi(self, DisplayProfile):
        DisplayProfile.setObjectName("DisplayProfile")
        DisplayProfile.setEnabled(True)
        DisplayProfile.resize(373, 474)
        DisplayProfile.setAutoFillBackground(True)
        DisplayProfile.setStyleSheet("background-color: rgb(190, 137, 255);\n"
"border-color: rgb(255, 14, 26);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(DisplayProfile)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 421))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayoutDP = QtWidgets.QVBoxLayout()
        self.verticalLayoutDP.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayoutDP.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayoutDP.setObjectName("verticalLayoutDP")
        self.Top_Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Top_Label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"")
        self.Top_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.Top_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Top_Label.setObjectName("Top_Label")
        self.verticalLayoutDP.addWidget(self.Top_Label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutDP.addItem(spacerItem1)
        self.input_link_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_link_label.setFont(font)
        self.input_link_label.setStyleSheet("color: rgb(255, 15, 39);")
        self.input_link_label.setTextFormat(QtCore.Qt.RichText)
        self.input_link_label.setObjectName("input_link_label")
        self.verticalLayoutDP.addWidget(self.input_link_label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(192, 244, 255);\n"
"font: 10pt \"Javanese Text\";\n"
"border-color: rgb(119, 255, 128);")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutDP.addWidget(self.lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayoutDP.addItem(spacerItem2)
        self.ok_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda : dp_download())
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok_button.setFont(font)
        self.ok_button.setMouseTracking(False)
        self.ok_button.setAutoFillBackground(False)
        self.ok_button.setStyleSheet("background-color: rgb(164, 37, 255);\n"
"border-color: rgb(16, 16, 255);")
        self.ok_button.setObjectName("ok_button")
        self.verticalLayoutDP.addWidget(self.ok_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutDP.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayoutDP)
        spacerItem4 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)

        self.retranslateUi(DisplayProfile)
        QtCore.QMetaObject.connectSlotsByName(DisplayProfile)

        def dp_download():
            print("ok")
            try :
                loader = instaloader.Instaloader()
                account = self.lineEdit.text()
                loader.download_profile(account, profile_pic_only = True)
                
                               
                print("task Completed ---> Check your directory ")
            except :
                print("enter valid profile name")

    def retranslateUi(self, DisplayProfile):
        _translate = QtCore.QCoreApplication.translate
        DisplayProfile.setWindowTitle(_translate("DisplayProfile", "Dp Download"))
        self.Top_Label.setText(_translate("DisplayProfile", "Dp Downloader"))
        self.input_link_label.setText(_translate("DisplayProfile", "Name of Person for DP :"))
        self.ok_button.setText(_translate("DisplayProfile", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayProfile = QtWidgets.QWidget()
    ui = Ui_DisplayProfile()
    ui.setupUi(DisplayProfile)
    DisplayProfile.show()
    sys.exit(app.exec_())

