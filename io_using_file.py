poem = '''\
Programming is fun
When the work is done
if u wanna make ur work also fun:
	use Python!!!!
'''
# Open for 'w'riting
f = open('poem.txt','w')
f.write(poem)
f.close()

# If no mode is specified
# 'r'ead mode is assumed by default

f = open('poem.txt')
while True:
	line = f.readline()
	if len(line) == 0 :
		break;
	print line
f.close()

