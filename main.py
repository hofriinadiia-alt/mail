import smtplib
from email.mime.text import MIMEText
import os

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

def send_test_email():
    msg = MIMEText("Hello from Render 🚀")
    msg["From"] = "admin@booking.com"   # будь-який spoof
    msg["To"] = "admin@domerascents.com"
    msg["Subject"] = "Render Test Email"

    server = smtplib.SMTP(SMTP_HOST, 587)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.send_message(msg)
    server.quit()

send_test_email()
print("Email sent!")
