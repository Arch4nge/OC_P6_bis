#!/usr/bin/python3

# Importing python dependances
import json
import ovh
import os

# LOADING specifics environement variables
APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
domain = os.getenv('DOMAIN')
id = os.getenv('RECORD_ID')

# Establishing connexion with OVH api
client = ovh.Client(
    endpoint='ovh-eu',
    application_key=APP_KEY,
    application_secret=APP_SECRET,
    consumer_key=CONSUMER_KEY,
)

# Deleting record after certbot verification
client.delete('/domain/zone/%s/record/%d' %(domain, id))
