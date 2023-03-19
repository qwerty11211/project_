
import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token") 
client = Client(account_sid, auth_token)


def send__message(text):
    message = client.messages.create(
        body=text,
        from_="+18507893715",
        to= os.environ.get("number") 
    )

def send_voice_call(text):
    response = VoiceResponse()
    response.say(text, voice='alice')
    response.record(timeout=10, transcribe=True)
    call = client.calls.create(
        twiml=response,
        from_='+18507893715',
        to=os.environ.get("number") 
    )
