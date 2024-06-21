#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf vote*')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('vote'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/vote?raw=true -o vote')
        os.system('chmod 777 vote')
        os.system('./vote')
    else:
        os.system('./vote')
elif bit == '32bit':
    if not os.path.isfile('vote32'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/vote32?raw=true -o vote32')
        os.system('chmod 777 vote32')
        os.system('./vote32')
    else:
        os.system('./vote32')
else:
    print ('Your device is not supported ')
    exit()
