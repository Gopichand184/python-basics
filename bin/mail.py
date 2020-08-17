import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_email = "chandunaidu184@gmail.com"
rec_email = 'gopichandu.paladugu@gmail.com'
# with open("/Users/apple/Desktop/ids.txt",'r')as data:
#     d = data.read()
#     rec_email.append(d.replace('\n', ''))
#     data.close()
# sub = "Python email"
password = getpass.getpass(prompt="please enter your password : ")
# msg = MIMEMultipart()
# msg['from'] = sender_email
# msg['To'] = rec_email
# msg['subject'] = sub
# body = "Hi chandu\n How are you.. This is python code generated email..having subject "
# msg.attach(MIMEText(body,'plain'))
# text = msg.as_string()
message = "Hi charan how are you"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("login sucess")
server.sendmail(sender_email,rec_email,message)
print("email has been sent to ",rec_email)

