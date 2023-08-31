from Camera.camera import get_frame, frame_to_image
from Neural_network.build_model import Model
from PIL import Image
from Notifications.send_mail import gmail_sender, login, content_for_fire_detection
from Notifications.phone_call import Caller
from User import User


def main():
    user = User(input("Enter your height of the drone please:"), input("Enter your speed of the drone please:"))
    counter_of_fire_frames = 0
    fire_images = []
    model = Model()
    caller = Caller()
    session = login()
    while True:
        frame = get_frame()
        image = Image.fromarray(frame)
        prediction = model.predict(image)
        if prediction:
            counter_of_fire_frames += 1
            image_to_send = frame_to_image(frame)
            fire_images.append(image_to_send)
            print("Fire detected")
        elif counter_of_fire_frames > 0:
            calculate_distance = user.calculate_distance(counter_of_fire_frames)
            mail_content = content_for_fire_detection(fire_images, calculate_distance)
            gmail_sender(session, mail_content)
            caller.call()
            break


if __name__ == "__main__":
    main()

