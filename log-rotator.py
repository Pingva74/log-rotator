import os 
import re
from shutil import copyfile
import time
from datetime import datetime

log_access = 'access_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.log'
path = '/home/alex/powershell/log.rotator/test'
now = time.time()
sawed_cwd = os.getcwd()
os.chdir(path)
copyfile('access.log', log_access)

log_error = 'error_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.log'
path = '/home/alex/powershell/log.rotator/test'
now = time.time()
sawed_cwd = os.getcwd()
os.chdir(path)
copyfile('error.log', log_error)


f = open('access.log', 'w')
f.seek(0)
f.close()

f = open('error.log', 'w')
f.seek(0)
f.close()



for filename in os.listdir(path):
    filestamp = os.stat(os.path.join(path, filename)).st_mtime
    filecompare = now - 180
    if  filestamp < filecompare:
       if re.match(r'access_', filename) is not None:
         os.remove(filename)
       if re.match(r'error_', filename) is not None:
         os.remove(filename)

os.chdir(sawed_cwd)
