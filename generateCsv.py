import csv

class GenerateCsv():
    def __init__(self, subject_name, subject_date, attendance):
        self.subject_name = subject_name
        self.subject_date = subject_date
        self.attendance = attendance

    #CSV FILE GENERATOR
    def generate_csv(self):
        a_file = open(self.subject_name+"_"+self.subject_date+"_Attendance"+".csv", "w",newline='')
        writer = csv.writer(a_file)
        writer.writerow(["NAME'S", "ATTENDANCE PERCENTAGE", "STATUS"])

        for key, value in self.attendance.items():
            value = (value/self.attendance['snapshot']) * 100
            s = format(value, '.2f')
            state = "ABSENT"
            if(value < 70):
                state = "ABSENT"
            else:
                state = "PRESENT"   
            if key is not 'snapshot' or 'Joined':    
                writer.writerow([key, s+"%", state])

        a_file.close()          