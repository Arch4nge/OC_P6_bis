#!/usr/bin/python3

import os

domain = 'example.com'
os.environ['DOMAIN'] = domain
os.environ['SUB_DOMAIN'] = 'test'
os.environ['RECORD'] = 'Hello world'

smbUser = "Username"
smbPassword = 'Password'
#smbClientMachinename = ''          # Option
smbServer = 'DESKTOP-XXXXX'
smbShare = 'c$'
smbIp = '10.0.0.0'
smbPort = '139'                     # Default are 139 or 445
path = ''
filename = 'test.txt'
os.environ['SMB_USER'] = smbUser
os.environ['SMB_PASSWORD'] = smbPassword
os.environ['SMB_SERVER'] = smbServer
os.environ['SMB_PORT'] = smbPort
os.environ['SMB_SHARE'] = smbShare
os.environ['SMB_IP'] = smbIp

#have you imported env variables and install requirements (python and apt)?

os.system('certbot certonly -n --preferred-challenge dns --manual --manual-auth-hook ./auth.py --manual-cleanup-hook ./clean.py --manual-public-ip-logging-ok -d *.%s', domain)

execfile("auth.py")

execfile("clean.py")

conn = SMBConnection(smbUser, smbPassword, smbClientMachinename, smbServer, use_ntlm_v2 = True)
conn.connect(smbIp, smbPort)
file2transfer = open(filename,"br")
value = conn.storeFile(smbShare,path + filename, file2transfer)
print ("%d Bytes was written", value)

os.system("net rpc restart Apache2.4 --ipaddress %d --user %s%%%s", smbIp, smbUser, smbPassword) #Restart required service
