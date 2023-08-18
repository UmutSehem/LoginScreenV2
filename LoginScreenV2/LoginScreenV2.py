import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from window import MainWindow
from register import RegisterApp
from forgotpass import ForgotApp

        

class LoginWindow(QtWidgets.QWidget):
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
        self.label.setGeometry(QtCore.QRect(260, 80, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(74)
        font.setBold(True)
        font.setWeight(74)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.label.setText("Sign Up")

        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(190,160,201,31))
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
        self.password.setGeometry(QtCore.QRect(190,220,201,31))
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

        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(220, 260, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(156, 170, 177);")
        self.login_button.setText("Login")

        
        self.forgotpas_button = QtWidgets.QPushButton(self.frame)
        self.forgotpas_button.setGeometry(QtCore.QRect(20, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.forgotpas_button.setFont(font)
        self.forgotpas_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgotpas_button.setStyleSheet("border-radius:3px;\n"
"background-color: rgb(156, 170, 177);")
        self.forgotpas_button.setText("🔑")

        
        self.register_button = QtWidgets.QPushButton(self.frame)
        self.register_button.setGeometry(QtCore.QRect(90, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.register_button.setFont(font)
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_button.setStyleSheet("border-radius:3px;\n"
"background-color: rgb(156, 170, 177);\n"
"")
        self.register_button.setText("📲")
        


        
        
        

        





        

        
                       
        










        
        
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("5509636.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("(_SHM_)LoginScreenV2")
        
        self.setStyleSheet("background-color: rgb(156, 170, 177);")
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setMinimumSize(638,490)
        self.setMaximumSize(638,490)
        
        self.login_button.clicked.connect(self.loginn)
        self.register_button.clicked.connect(self.registerr)
        self.forgotpas_button.clicked.connect(self.forgotpassword)
        
        self.show()




    def loginn(self):
        ka = self.email.text()
        par = self.password.text()

        self.cursor.execute("SELECT * FROM member WHERE EMAİL = ? AND PASSWORD = ?", (ka, par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            print("Not Found User!")
            self.email.clear()
            self.password.clear()
        else:
                self.close()
                self.new_window = MainWindow()
                self.new_window.show()


    def registerr(self):
        self.new_window2 = RegisterApp()
        self.new_window2.show()
    
    def forgotpassword(self):
        self.new_window3 = ForgotApp()
        self.new_window3.show()







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    sys.exit(app.exec())