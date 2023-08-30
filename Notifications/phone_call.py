from twilio.rest import Client


def Caller():
    def __init__(self):
        # Your Account SID from twilio.com/console
        account_sid = "AC1792366dc309d512d311d636fdbaf0e6"
        # Your Auth Token from twilio.com/console
        auth_token = "1478aaee9a35288abb5c0723e9e35a8e"

        self.client = Client(account_sid, auth_token)

    def call(self):
        call = self.client.calls.create(
            from_='97233820813',
            to='+972507245538',
            url='https://handler.twilio.com/twiml/EH5d6503768fcb97e18e107030bf9d3cec'
        )