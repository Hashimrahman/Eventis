import os
import smtplib
from email.message import EmailMessage

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_FROM_NAME = os.getenv("EMAIL_FROM_NAME")


def send_verification_email(to_email: str, token: str):
    msg = EmailMessage()
    msg["Subject"] = "Verify your email"
    msg["From"] = f"{EMAIL_FROM_NAME} <{EMAIL_FROM}>"
    msg["To"] = to_email

    verification_link = f"http://localhost:8000/api/v1/auth/verify-email?token={token}"
    msg.set_content(
        f"Click the link below to verify your email:\n\n{verification_link}"
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)


def send_reset_password_email(to_email: str, token: str):
    msg = EmailMessage()
    msg["Subject"] = "Reset your password"
    msg["From"] = f"{EMAIL_FROM_NAME} <{EMAIL_FROM}>"
    msg["To"] = to_email

    reset_link = f"http://localhost:8000/api/v1/auth/reset-password?token={token}"
    msg.set_content(f"Click the link below to reset your password:\n\n{reset_link}")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
