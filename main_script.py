#!/usr/bin/python3

import os

domain = os.getenv('DOMAIN')
sub_domain = os.getenv('SUB_DOMAIN')
smbUser = os.getenv('SMB_USER')
smbPassword = os.getenv('SMB_PASSWORD')
smbClientMachinename = os.getenv('SMB_CLIENTMACHINENAME')
smbServer = os.getenv('SMB_SERVER')
smbShare = os.getenv('SMB_SHARE')
smbIp = os.getenv('SMB_IP')
smbPort = os.getenv('SMB_PORT')
sourcePath = os.getenv('SOURCE_PATH')
destPath = os.getenv('DEST_PATH')
filename1 = os.getenv('FILENAME1')
filename2 = os.getenv('FILENAME2')
# LOADING all variables environement

os.system('certbot certonly -n --preferred-challenge dns --manual --manual-auth-hook ./auth.py --manual-cleanup-hook ./clean.py --manual-public-ip-logging-ok -d *.%s', domain)
# Generating certificates

conn = SMBConnection(smbUser, smbPassword, smbClientMachinename, smbServer, use_ntlm_v2 = True)
conn.connect(smbIp, smbPort)
# Establishing samba connexion

file2transfer = open(sourcePath + '/' + sub_domain + '.' + domain + '/' + filename1,"br")
value = conn.storeFile(smbShare,destPath + '/' + filename1 , file2transfer)
print ("%d Bytes was written for file 1", value)
# Copying first file (fullchain.pem)

file2transfer = open(sourcePath + '/' + sub_domain + '.' + domain + '/' + filename2,"br")
value = conn.storeFile(smbShare,destPath + '/' + filename2 , file2transfer)
print ("%d Bytes was written for file 2", value)
# Copying second file (privkey.pem)

os.system("net rpc restart Apache2.4 --ipaddress %d --user %s%%%s", smbIp, smbUser, smbPassword) #Restart required service
# Restarting apache to use new certificates