import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template

# Email configuration
FROM_EMAIL = 'myemail@gmail.com'
PASSWORD = 'password'  # testing with personal gmail account, this is app_password
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
TO_EMAIL = 'receiver_address@addr.com'

# Email content
SUBJECT = 'Hello Email World!'
BODY = render_template('HtmlEmail.html')

# Create message
msg = MIMEMultipart()
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = SUBJECT
msg.attach(MIMEText(BODY, 'html'))

# Send email
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(FROM_EMAIL, PASSWORD)
server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
server.quit()

print('Email sent successfully!')



# Effectively using smtp to send simple email, html template.