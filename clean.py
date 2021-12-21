#!/usr/bin/python3

import json
import ovh
import os

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
domain = os.getenv('DOMAIN')

client = ovh.Client(
    endpoint='ovh-eu',
    application_key=APP_KEY,
    application_secret=APP_SECRET,
    consumer_key=CONSUMER_KEY,
)

client.delete('/domain/zone/%s/record/%d' %(domain, id['id']))