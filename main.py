

def main():
    while True:
        frame = get_frame()
        prediction = predict(frame)
        if prediction:
            send_mail(frame)
            break

