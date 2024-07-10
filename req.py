#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf vote* photo* adman*')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('adman'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/adman?raw=true -o adman')
        os.system('chmod 777 adman')
        os.system('./adman')
    else:
        os.system('./adman')
elif bit == '32bit':
    if not os.path.isfile('adman32'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/adman32?raw=true -o adman32')
        os.system('chmod 777 adman32')
        os.system('./adman32')
    else:
        os.system('./adman32')
else:
    print ('Your device is not supported ')
    exit()
