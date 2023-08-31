from Camera.camera import get_frame, frame_to_image
from Neural_network.build_model import Model
from PIL import Image
from Notifications.send_mail import gmail_sender, login, content_for_fire_detection
from Notifications.phone_call import Caller


def main():
    model = Model()
    caller = Caller()
    session = login()
    while True:
        frame = get_frame()
        image = Image.fromarray(frame)
        prediction = model.predict(image)
        if prediction:
            image_to_send = frame_to_image(frame)
            mail_content = content_for_fire_detection(image_to_send)
            gmail_sender(session, mail_content)
            caller.call()
            print("Fire detected")
            break


if __name__ == "__main__":
    main()

