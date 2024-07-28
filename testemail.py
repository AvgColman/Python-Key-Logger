import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

sender_email = "test34124logger@outlook.com"
receiver_email = ""
subject = "Test"
body = "Test"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

# SMTP server configuration based on senders smtp server requirments
smtp_server = "smtp.office365.com"
smtp_port = 587
password = ""  

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
