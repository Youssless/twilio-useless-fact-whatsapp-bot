import json
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    quote = ""

    if 'useless fact' in incoming_msg:
        response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')

        if response.status_code == 200:
            data = response.json()
            quote = f'{data["text"]} \nreference: {data["source_url"]}'
        else:
            quote = 'An unknown error has occured'
    else:
        quote = "Hi there! Type \'useless fact\'"

    msg.body(quote)

    return str(resp)

if __name__ == '__main__':
    app.run()


    
