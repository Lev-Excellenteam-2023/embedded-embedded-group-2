# import the opencv library
from email.mime.image import MIMEImage
import cv2



def get_frame():
    """
    Capture a video frame, encode it to JPEG format, and return it as a MIMEImage object.

    This function captures a single frame from a video source, converts the frame data
    to JPEG format, and packages it as a MIMEImage object suitable for attachment in an email.

    :return: A MIMEImage object containing the encoded video frame.
    :rtype: email.mime.image.MIMEImage
    """
    # Capture the video frame
    # define a video capture object
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return frame


def frame_to_image(frame):
    # Convert the frame data to bytes
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()

    # Attach the frame bytes to the email
    image = MIMEImage(frame_bytes, name='image.jpg')
    return image


if __name__ == '__main__':
    get_frame()