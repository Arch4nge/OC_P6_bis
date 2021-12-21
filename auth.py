#!/usr/bin/python3

import json
import ovh
import os

domain = os.getenv('DOMAIN')
subDomain = os.getenv('SUB_DOMAIN')
record = os.getenv('RECORD')

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')

client = ovh.Client(
    endpoint='ovh-eu',
    application_key=APP_KEY,
    application_secret=APP_SECRET,
    consumer_key=CONSUMER_KEY,
)

id = client.post('/domain/zone/%s/record' %(domain), 
    fieldType='TXT', #// Resource record Name (type: zone.NamedResolutionFieldTypeEnum)
    subDomain=subDomain, #// Resource record subdomain (type: string)
    target=record, #// Resource record target (type: string)
    ttl='0', #// Resource record ttl (type: long)
)

os.environ['RECORD_ID'] = id['id']

print (id['id'])
client.delete('/domain/zone/%s/record/%d' %(domain, id['id']))