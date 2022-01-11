# OpenClassrooms Project 6
A powerful script to create certificates with letsencrypt using certbot.

The validation for the certificates is done using DNS record with OVH.

Then the certificates is pushed on a remote windows host using samba.


# How to run the script
Basically you need to do 3 things :
- Install dependances for the script
- Loads environement variables and custom variable in the script
- Run main_script.py


# Install requirements
Run ```pip3 install -r ./requirements.txt```

Ensure that your remote windows host has a samba server enable.

Your local host must have certbot installed.

Also please note that this script use OVH as cloud provider in order to validate the letsencrypt operation.

Note that you also need credentials from https://api.ovh.com/ in order to validate your certificates.

# Customisation of the script
All variables you would like to change are in 1 location only:
 - env (either in .env file either in your environement directly) the env contain info about your ovh credentials and all variables used in the script

just cp the original .env.example file into your own .env file :
```
cp .env.example .env
```

And load this .env file
```
export $(cat .env)
```

# Attention

Be careful, to replace the placeholder in both main_script.py and env value before starting the script

# Possible enhancements

Implementation of another DNS provider

Multiple windows hosts supports for one certificate

Multiple certificates handling

Daemonize it ! (renew each certificates before they expires)