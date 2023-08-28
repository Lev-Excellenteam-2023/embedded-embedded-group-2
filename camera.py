# import the opencv library
from email.mime.image import MIMEImage

import cv2
import imageio.v3 as iio

# define a video capture object
vid = cv2.VideoCapture(0)


def get_frame():
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Convert the frame data to bytes
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()

    # Attach the frame bytes to the email
    image = MIMEImage(frame_bytes, name='frame.jpg')

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return image


if __name__ == '__main__':
    get_frame()