#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf vote.so vote32.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('vote.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/vote.cpython-311.so?raw=true -o vote.so')
        os.system('chmod 777 vote.so')
        from vote import main
        main()
    else:
        from vote import main
        main()
elif bit == '32bit':
    if not os.path.isfile('vote32.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/vote32.cpython-311.so?raw=true -o vote32.so')
        os.system('chmod 777 vote32.so')
        from vote32 import main
        main()
    else:
        from vote32 import main
        main()
else:
    print ('Your device is not supported ')
    exit()
