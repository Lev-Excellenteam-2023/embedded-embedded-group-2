import smtplib
import time
from consts import SENDER, RECEIVER, PASSWORD, SUBJECT, CONTENT
from Camera.camera import get_frame
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def content_for_fire_detection(image):
    """
    Creates the email content for fire detection notification.

    Args:
        image (bytes): The image data in bytes.

    Returns:
        MIMEMultipart: A MIME multipart object containing email content.
    """

    # Create Headers
    email_data = MIMEMultipart()
    email_data['Subject'] = SUBJECT
    email_data['To'] = RECEIVER
    email_data['From'] = SENDER

    # Attach our text data
    email_data.attach(MIMEText(CONTENT + time.ctime()))

    # Create our Image Data from the defined image
    image_data = MIMEImage(image)
    image_data.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
    email_data.attach(image_data)

    return email_data


def login():
    """
    Establish an SMTP session, start TLS, and authenticate with Gmail SMTP server.

    This function creates an SMTP session to connect to the Gmail SMTP server using the provided
    sender email and password. It starts a TLS connection for security and performs
    authentication. If successful, the session object is returned.

    :return: An SMTP session object if authentication is successful, or None if an error occurs.
    :rtype: smtplib.SMTP or None
    """
    try:
        # creates SMTP session
        session = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        session.starttls()
        # Authentication
        session.login(SENDER, PASSWORD)
        return session
    except Exception as e:
        print("An error occurred:", e)


def gmail_sender(session, content):
    """
    Send an email using the provided SMTP session.

    This function uses the provided SMTP session to send an email with the specified content.
    It sends the email to the designated receiver using the sender's email address.
    After sending the email, it terminates the SMTP session.

    :param session: An active SMTP session.
    :type session: smtplib.SMTP
    :param content: The email content as a MIME object.
    :type content: email.mime.MIMEBase.MIMEBase
    """
    try:
        # Send the email using the provided session
        session.sendmail(SENDER, RECEIVER, content.as_string())
        # Terminate the SMTP session
        session.quit()
    except Exception as e:
        print("An error occurred while sending the email:", e)


if __name__ == '__main__':
    session = login()
    image_to_send = get_frame()
    gmail_sender(session, image_to_send)