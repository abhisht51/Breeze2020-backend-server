import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import sched
import webbrowser
import time

email_user = "admin@snu-breeze.com"
email_password = "ZaidPp5szePE"
email_send = "rohitagrawalcgartist@gmail.com"

subject = 'Welcome to Breeze Bitch'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = '<h1>Nigga Hi!</h1>'
msg.attach(MIMEText(body,'html'))
msg.add_header('reply-to', 'breeze@snu.edu.in')

text = msg.as_string()
server = smtplib.SMTP_SSL('SMTP.zoho.com',465)
# server.ehlo()
# server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user, email_send, text)
server.quit()