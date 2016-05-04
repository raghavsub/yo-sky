import os

import requests
from flask import Flask, request

app = Flask(__name__)

yo_token = 'e343b190-76ed-fc4f-a417-d410f7d0d0f0'
fc_token = 'c18918bbf6b5926ebea301daf2085b69'
ith_lat = '42.4433'
ith_long = '-76.5000'

@app.route('/')
def main():
    username = request.args.get('username')

    rain = False
    r = requests.get('https://api.forecast.io/forecast/' + fc_token + '/' + ith_lat + ',' + ith_long)
    for time in r.json()['minutely']['data']:
        if time['precipProbability'] >= .20:
            rain = True

    if rain:
        requests.post('https://api.justyo.co/yo/', {'api_token': yo_token, 'username': username})

    return ''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
