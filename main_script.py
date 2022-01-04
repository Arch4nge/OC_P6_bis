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

path = ''
filename = 'test.txt'
#have you imported env variables and install requirements (python and apt)?

os.system('certbot certonly -n --preferred-challenge dns --manual --manual-auth-hook ./auth.py --manual-cleanup-hook ./clean.py --manual-public-ip-logging-ok -d *.%s', domain)

conn = SMBConnection(smbUser, smbPassword, smbClientMachinename, smbServer, use_ntlm_v2 = True)
conn.connect(smbIp, smbPort)
file2transfer = open(filename,"br")
value = conn.storeFile(smbShare,path + filename, file2transfer)
print ("%d Bytes was written", value)

os.system("net rpc restart Apache2.4 --ipaddress %d --user %s%%%s", smbIp, smbUser, smbPassword) #Restart required service
