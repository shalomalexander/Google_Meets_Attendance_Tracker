from attendanceTrackerGui import Ui_AttendanceTrackerMainWindow
from scrapAttendance import ScrapAttendance
from generateCsv import GenerateCsv
from sendEmail import SendEmail
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
import os
from subprocess import Popen, PIPE
import datetime

class AttendanceTrackerRun(Ui_AttendanceTrackerMainWindow):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        myWindow = QtWidgets.QMainWindow()
        super().setupUi(myWindow)
        try:
            self.widget_data = self.load_widget_data()
            self.stop = False
            self.p1 = None
            # initilize widgets with data
            self.subject_comboBox.addItems(self.widget_data["subjects"])
            # add button functions
            self.start_pushButton.clicked.connect(self.start_scrap)
            self.stop_pushButton.clicked.connect(self.stop_scrap)
            self.send_mail_pushButton.clicked.connect(self.send_email)
            # show your window
            myWindow.show()
            sys.exit(app.exec_())

        except Exception as e:
            print("There is some error. Please Check your attendanceTracker.json is placed in the same folder as this program or not.")
            print(e)
            sys.exit(app.exec_())

    def load_widget_data(self):
        with open("attendanceTracker.json", "r") as f:
            content = json.load(f)
        return content

    def start_scrap(self):
        print("The Google Meets Attendance Tracker is starting...")
        self.p1 = Popen(["python",r"C:\Users\ShalomAlexander\Documents\Python\AttendanceTRacker\scrapAttendance.py"])


    def stop_scrap(self):
        print("The Google Meets Attendance Tracker is stopped...")
        if self.p1:
            self.p1.kill()
            subject_name = self.subject_comboBox.currentText()
            subject_date = str(datetime.date.today())
            with open('result.json') as json_file: 
                attendance = json.load(json_file)  
            generate_csv = GenerateCsv(subject_name, subject_date, attendance)       
            generate_csv.generate_csv()
            if os.path.exists("result.json"): 
                os.remove("result.json") 
            

    def send_email(self):
        email_id = self.email_lineEdit.text()
        subject_name = self.subject_comboBox.currentText()
        subject_date = str(datetime.date.today())
        email_subject = subject_name+" Attendance "+subject_date
        file_name = subject_name+"_"+subject_date+"_Attendance"+".csv"
        #print("dummy email function:", email_id)
        send_email = SendEmail(email_id, email_subject, file_name)



if __name__ == "__main__":
    obj = AttendanceTrackerRun()