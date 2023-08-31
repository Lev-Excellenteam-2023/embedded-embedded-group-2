from twilio.rest import Client
from consts import load_dotenv
import os


class Caller():
    def __init__(self):
        load_dotenv()
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(account_sid, auth_token)

    def call(self):
        self.client.calls.create(
            from_='97233820813',
            to='+972515476800',
            url='https://handler.twilio.com/twiml/EH5c29885042269b8451a70a1a0691d921'
        )

def main():
    caller = Caller()
    caller.call()


if __name__ == '__main__':
    main()