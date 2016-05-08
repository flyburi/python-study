name ='buri'

if name.startswith('bu'):
	print 'Yes, the string starts with "bu"'

if 'r' in name:
	print 'Yes, it contains the string "r"'
if name.find('ur') != -1:
	print 'Yes, it contains the string "ur"'

delimiter ='_*_'
mylist = ['Brazil','Russia','India','China']
print delimiter.join(mylist)
