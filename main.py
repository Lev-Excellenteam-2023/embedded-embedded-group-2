from Camera.camera import get_frame, frame_to_image
from Neural_network.build_model import Model
from PIL import Image
from send_mail import gmail_sender, login, content_for_fire_detection


def main():
    model = Model()
    session = login()
    while True:
        frame = get_frame()
        image = Image.fromarray(frame)
        prediction = model.predict(image)
        if True:
            image_to_send = frame_to_image(frame)
            mail_content = content_for_fire_detection(image_to_send)
            gmail_sender(session, mail_content)
            print("Fire detected")
            break


if __name__ == "__main__":
    main()

