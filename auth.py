#!/usr/bin/python3

# Importing python dependances
import json
import ovh
import os

# LOADING specifics environement variables
domain = os.getenv('DOMAIN')
subDomain = os.getenv('SUB_DOMAIN')
record = os.getenv('RECORD')
APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')

# Establishing connexion with OVH api
client = ovh.Client(
    endpoint='ovh-eu',
    application_key=APP_KEY,
    application_secret=APP_SECRET,
    consumer_key=CONSUMER_KEY,
)

# Create record for certbot verification
id = client.post('/domain/zone/%s/record' %(domain), 
    fieldType='TXT', #// Resource record Name (type: zone.NamedResolutionFieldTypeEnum)
    subDomain=subDomain, #// Resource record subdomain (type: string)
    target=record, #// Resource record target (type: string)
    ttl='0', #// Resource record ttl (type: long)
)

# Logging Record ID for deletion after verification
os.environ['RECORD_ID'] = id['id']