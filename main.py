from Camera.camera import get_frame, frame_to_image
from Neural_network.build_model import Model
from PIL import Image
from send_mail import gmail_sender, login


def main():
    model = Model()
    session = login()
    while True:
        frame = get_frame()
        image = Image.fromarray(frame)
        prediction = model.predict(image)
        if prediction:
            image_to_send = frame_to_image(frame)
            gmail_sender(session, image_to_send)
            print("Fire detected")
            break


if __name__ == "__main__":
    main()

