import smtplib
import time

from consts import SENDER, RECEIVER, PASSWORD, list_of_receivers, SUBJECT, CONTENT, Smtp_Server, Port

from Camera.camera import get_frame

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def content_for_fire_detection(images, size_of_fire):
    """
    Creates the email content for fire detection notification.

    Args:
        images (bytes): The images data in bytes.
        size_of_fire (int): The size of detected fire.

    Returns:
        MIMEMultipart: A MIME multipart object containing email content.
    """

    # Create Headers
    email_data = MIMEMultipart()
    email_data['Subject'] = SUBJECT
    #email_data['To'] = RECEIVER
    email_data['From'] = SENDER

    # Attach our text data
    email_data.attach(MIMEText(CONTENT + time.ctime() + str(size_of_fire) + ' meter'))

    # Create our Image Data from the defined image
    counter = 0
    for image in images:
        counter += 1
        image.add_header('Content-Disposition', 'attachment; filename="image{}.jpg"'.format(counter))
        email_data.attach(image)

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
        session = smtplib.SMTP(Smtp_Server, Port)
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
        for mail in list_of_receivers:
            content['To'] = mail
            session.sendmail(SENDER, mail, content.as_string())
        # Terminate the SMTP session
        session.quit()
    except Exception as e:
        print("An error occurred while sending the email:", e)


if __name__ == '__main__':
    session = login()
    image_to_send = get_frame()
    gmail_sender(session, image_to_send)