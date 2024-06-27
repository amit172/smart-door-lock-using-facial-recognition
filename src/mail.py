import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'doorkeeper420@gmail.com'
    msg['To'] = 'amit1joshi1997@gmail.com'
    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)
    port=smtplib.SMTP_PORT
    s = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('doorkeeper420@gmail.com', '********')
    From = msg['From']
    To = msg['To']
    s.sendmail(From, To, msg.as_string())
    s.quit()

FileName = 'ImageBase/Amit Joshi.jpg'
SendMail(FileName)
