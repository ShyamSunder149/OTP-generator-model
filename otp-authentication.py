import random
import smtplib
from email.message import EmailMessage

randomNumber = random.randint(100000,999999)

sender_email = "REDACTED"
sender_password = "REDACTED"

receiver_email = "REDACTED"

msg = EmailMessage()
msg.set_content('''
\n
Hey User,
Your OTP is {}
\n
'''.format(randomNumber))

msg['Subject'] = 'One Time Password'
msg['From'] = sender_email
msg['To'] = receiver_email

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email,sender_password)
server.send_message(msg)
server.quit()
print('otp sent to mail')


x = int(input("enter the otp:"))
if x == randomNumber:
    print("Success")
else:
    print("Failure")