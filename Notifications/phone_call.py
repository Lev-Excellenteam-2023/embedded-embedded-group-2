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
            to='+972507245538',
            url='https://handler.twilio.com/twiml/EH5d6503768fcb97e18e107030bf9d3cec'
        )

def main():
    caller = Caller()
    caller.call()


if __name__ == '__main__':
    main()