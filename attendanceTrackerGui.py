# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attendanceTrackerGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AttendanceTrackerMainWindow(object):
    def setupUi(self, AttendanceTrackerMainWindow):
        AttendanceTrackerMainWindow.setObjectName("AttendanceTrackerMainWindow")
        AttendanceTrackerMainWindow.resize(754, 230)
        AttendanceTrackerMainWindow.setMinimumSize(QtCore.QSize(754, 230))
        AttendanceTrackerMainWindow.setMaximumSize(QtCore.QSize(16777215, 500))
        self.centralwidget = QtWidgets.QWidget(AttendanceTrackerMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subject_label = QtWidgets.QLabel(self.centralwidget)
        self.subject_label.setMaximumSize(QtCore.QSize(50, 50))
        self.subject_label.setObjectName("subject_label")
        self.horizontalLayout.addWidget(self.subject_label)
        self.subject_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.subject_comboBox.setObjectName("subject_comboBox")
        self.horizontalLayout.addWidget(self.subject_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_lineEdit.setMaximumSize(QtCore.QSize(675, 16777215))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.horizontalLayout_2.addWidget(self.email_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout_3.addWidget(self.start_pushButton)
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.horizontalLayout_3.addWidget(self.stop_pushButton)
        self.send_mail_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.send_mail_pushButton.setObjectName("send_mail_pushButton")
        self.horizontalLayout_3.addWidget(self.send_mail_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        AttendanceTrackerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AttendanceTrackerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 26))
        self.menubar.setObjectName("menubar")
        AttendanceTrackerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AttendanceTrackerMainWindow)
        self.statusbar.setObjectName("statusbar")
        AttendanceTrackerMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AttendanceTrackerMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AttendanceTrackerMainWindow)

    def retranslateUi(self, AttendanceTrackerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AttendanceTrackerMainWindow.setWindowTitle(_translate("AttendanceTrackerMainWindow", "Google Meets - Attendance Tracker "))
        self.subject_label.setText(_translate("AttendanceTrackerMainWindow", "Subject"))
        self.label.setText(_translate("AttendanceTrackerMainWindow", "Email"))
        self.start_pushButton.setText(_translate("AttendanceTrackerMainWindow", "Start"))
        self.stop_pushButton.setText(_translate("AttendanceTrackerMainWindow", "Stop"))
        self.send_mail_pushButton.setText(_translate("AttendanceTrackerMainWindow", "Send Mail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AttendanceTrackerMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AttendanceTrackerMainWindow()
    ui.setupUi(AttendanceTrackerMainWindow)
    AttendanceTrackerMainWindow.show()
    sys.exit(app.exec_())

