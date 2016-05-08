import os
import time

source =['/Users/buri/dev/dev-python/byte_of_python/python-study']

target_dir='/Users/buri/dev/dev-python/byte_of_python/python-study-backup'

target = target_dir + os.sep + time.strftime('%y%m%d%H%M%S')+'.zip'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

print "Zip command is:"
print zip_command
print "Running:"
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup Failed.'

