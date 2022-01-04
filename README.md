# OpenClassrooms Project 6
A powerful script to create certificates with letsencrypt using certbot.

The validation for the certificates is done using DNS record with OVH.

Then the certificates is pushed on a remote wçndows host using samba.


# How tu run the script
Basically you need to do 3 things :
- Install dependances for the script
- Loads environement variables and custom variable in the script
- Run main_script.py


# Load requirement
Run ```pip3 install -r ./requirements.txt```

Ensure that your remote windows host has a samba server enable.

Your local host must have certbot installed.

Also please note that this script use OVH as cloud provider in order to validate the letsencrypt operation.


# Customisation of the script
All variables you would like to change are in 2 location:
 - main_script.py (Contains all infos about remote windows server where you want to renew the certificate)
 - env (either in .env file either in your environement directly) the env contain info about your ovh credentials

example of .env file :
```
APP_KEY="xxx"
APP_SECRET="yyy"
CONSUMER_KEY="zzz"
```

# Attention

Be careful, to replace the placeholder in both main_script.py and env value before starting the script
