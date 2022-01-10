# Importing all required file and Hedderfiles
from PyQt5 import QtCore, QtGui, QtWidgets
from InstagramAPI import InstagramAPI

class Ui_Upload(object):
    def setupUi(self, Upload):
        # setting up of Layouts
        Upload.setObjectName("Upload")
        Upload.setWindowModality(QtCore.Qt.NonModal)
        Upload.resize(356, 403)
        Upload.setStyleSheet("background-color: rgb(255, 166, 232);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Upload)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 341, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # Top hedding of Screen
        self.Top_Level = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Top_Level.setStyleSheet("color: rgb(255, 43, 15);\n"
"font: 24pt \"Verdana\";")
        self.Top_Level.setAlignment(QtCore.Qt.AlignCenter)
        self.Top_Level.setObjectName("Top_Level")
        self.verticalLayout.addWidget(self.Top_Level)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        # This will display info over Id Input
        self.ID_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ID_label.setStyleSheet("color: rgb(56, 16, 255);\n"
"font: 75 14pt \"Palatino Linotype\";")
        self.ID_label.setObjectName("ID_label")
        self.verticalLayout.addWidget(self.ID_label)
        # Taking input from user (email or phone number)
        self.IDInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.IDInput.setStyleSheet("background-color: rgb(230, 225, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.IDInput.setObjectName("IDInput")
        self.verticalLayout.addWidget(self.IDInput)
        # Password Lable
        self.Password = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Password.setStyleSheet("color: rgb(37, 48, 255);\n"
"font: 75 14pt \"Palatino Linotype\";")
        self.Password.setObjectName("Password")
        self.verticalLayout.addWidget(self.Password)
        # Take Passsword Input from user
        self.passwordInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.passwordInput.setStyleSheet("background-color: rgb(230, 225, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.passwordInput.setObjectName("passwordInput")
        self.verticalLayout.addWidget(self.passwordInput)
        # post lable 
        self.post_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.post_label.setStyleSheet("color: rgb(37, 48, 255);\n"
"font: 75 14pt \"Palatino Linotype\";")
        self.post_label.setObjectName("post_label")
        self.verticalLayout.addWidget(self.post_label)
        # Taking uploading post Path from User
        self.postLink = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.postLink.setStyleSheet("background-color: rgb(230, 225, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Sans Serif\";")
        self.postLink.setObjectName("postLink")
        self.verticalLayout.addWidget(self.postLink)
        spacerItem2 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        # Defining Push Button which will send all info to function postupload
        self.loginPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda : postupload())
        self.loginPushButton.setStyleSheet("background-color: rgb(209, 117, 255);\n"
"font: 75 11pt \"Perpetua Titling MT\";\n"
"color: rgb(0, 0, 255);")
        self.loginPushButton.setObjectName("loginPushButton")
        self.verticalLayout.addWidget(self.loginPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)

        self.retranslateUi(Upload)
        QtCore.QMetaObject.connectSlotsByName(Upload)

        def postupload():
            '''This function will take all data and upload given pic in profile'''
            try:
                #Trying to Login
                # Login id
                log = self.IDInput.text()
                # Password
                pas = self.passwordInput.text()
                InstagramAPI = InstagramAPI(log, pas)
                # login
                InstagramAPI.login()
            except :
                # If dosent Login then give error
                print("Plz type correct UserName and Password")

            photo_path = self.postLink.text()
            caption = "Sample photo"
            try :
                #Trying to upload Photo
                InstagramAPI.uploadPhoto(photo_path, caption=caption)
            except:
                # if error execute
                print("Give Right Path of photo !!!")
            

    def retranslateUi(self, Upload):
        _translate = QtCore.QCoreApplication.translate
        Upload.setWindowTitle(_translate("Upload", "Post Uploader"))
        self.Top_Level.setText(_translate("Upload", "Uploading Post"))
        self.ID_label.setText(_translate("Upload", "Login ID :"))
        self.Password.setText(_translate("Upload", "Password :"))
        self.post_label.setText(_translate("Upload", "Type Image Present complete Path:"))
        self.loginPushButton.setText(_translate("Upload", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Upload = QtWidgets.QWidget()
    ui = Ui_Upload()
    ui.setupUi(Upload)
    Upload.show()
    sys.exit(app.exec_())

