from Camera.camera import get_frame, frame_to_image
from Neural_network.build_model import Model
from send_mail import gmail_sender, login


def main():
    session = login()
    while True:
        frame = get_frame()
        prediction = Model.predict(frame)
        if prediction:
            image_to_send = frame_to_image(frame)
            gmail_sender(session, image_to_send)
            break

