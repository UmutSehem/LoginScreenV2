import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


        

class RegisterApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()

    def connect_db(self):
        self.database_connect = sqlite3.connect("member.db")
        self.cursor = self.database_connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS member (EMAİL TEXT, PASSWORD TEXT)")
        self.database_connect.commit()

    def init_ui(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 29, 601, 431))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:35px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 80, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(74)
        font.setBold(True)
        font.setWeight(74)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.label.setText("Registering")

        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(190,150,201,31))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.email.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.email.setPlaceholderText("🔒E-mail")
        self.email.setMaxLength(20)

        self.email.setText("")

        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(190,210,201,31))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.password.setPlaceholderText("🔒Password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setMaxLength(5)
        self.password.setText("")

        self.conf_password = QtWidgets.QLineEdit(self.frame)
        self.conf_password.setGeometry(QtCore.QRect(190,270,201,31))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.conf_password.setFont(font)
        self.conf_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conf_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.conf_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.conf_password.setPlaceholderText("🔒Confirm Password")
        self.conf_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conf_password.setMaxLength(5)
        self.conf_password.setText("")

        self.register_Button = QtWidgets.QPushButton(self.frame)
        self.register_Button.setGeometry(QtCore.QRect(220, 310, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.register_Button.setFont(font)
        self.register_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_Button.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(156, 170, 177);")
        self.register_Button.setText("Register")

        


        
        
        

        





        

        
                       
        










        
        
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("5509636.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("(_SHM_)RegisterScreen")
        
        self.setStyleSheet("background-color: rgb(156, 170, 177);")
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setMinimumSize(638,490)
        self.setMaximumSize(638,490)
        

        self.register_Button.clicked.connect(self.registerr)
        
        self.show()

    def registerr(self):
        username = self.email.text()
        password = self.password.text()
        conf_password = self.conf_password.text()

        if not username or not password or not conf_password:
            print("Please fill in all fields.")
            return
        else:
            self.cursor.execute("SELECT * FROM member WHERE EMAİL = ?", (username,))
            existing_user = self.cursor.fetchone()
            if existing_user:
                self.email.clear()
                print("Such a User Already Exists!\nPlease Try Again!")
            elif password == conf_password:
                self.cursor.execute("INSERT INTO member (EMAİL, PASSWORD) VALUES (?, ?)", (username, password))
                self.database_connect.commit()
                print("Registration Success!")
                self.close()
            else:
                print("Passwords Do Not Match!")
                self.email.clear()
                self.password.clear()
                self.conf_password.clear()
