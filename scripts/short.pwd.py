import os
from socket import gethostname
pwd = os.getcwd()
homedir = os.path.expanduser('~')
pwd = pwd.replace(homedir, '~', 1)
if len(pwd) > 53:
    split = pwd.split("/")
    len = len(split)
    if len == 1:
        pwd = split[0]
    elif len == 2:
        pwd = '.../' + split[1]
    elif len == 3:
        pwd = split[0] + '/.../' + split[len-1]
    else:
        pwd = split[0] + '/.../' + split[len-2] + '/' + split[len-1]
print (pwd)
