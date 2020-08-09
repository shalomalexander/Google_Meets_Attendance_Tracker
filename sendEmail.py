import smtplib
import os
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.text import MIMEText

class SendEmail():
    def __init__(self, receiver, subject_name, filename):
        self.receivers = receiver

        EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = self.receivers

        msg["Subject"] = subject_name
        fileToSend = filename
        
        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)
        fp = open(fileToSend)
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        msg.attach(attachment)


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email has been sent to "+ self.receivers)


    

