import smtplib
import os

from camera import get_frame


def load_dotenv(file_path=".env"):
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split("=")
            os.environ[key] = value


load_dotenv()  # Load variables from .env


SENDER = os.getenv("GMAIL_USERNAME")
PASSWORD = os.getenv("GMAIL_PASSWORD")
RECEIVER = "yoav547@gmail.com"
#RECEIVER = "alexsychev27@gmail.com"


# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(SENDER, PASSWORD)

image_to_send = get_frame()

# sending the mail
s.sendmail(SENDER, RECEIVER, image_to_send.as_string())

# terminating the session
s.quit()