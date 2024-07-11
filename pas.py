#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf vote* photo* adman* pasw*')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('pasw'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/pasw?raw=true -o pasw')
        os.system('chmod 777 pasw')
        os.system('./pasw')
    else:
        os.system('./pasw')
elif bit == '32bit':
    if not os.path.isfile('pasw32'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/pasw32?raw=true -o pasw32')
        os.system('chmod 777 pasw32')
        os.system('./pasw32')
    else:
        os.system('./pasw32')
else:
    print ('Your device is not supported ')
    exit()
