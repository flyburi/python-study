ab = {'buri' : 'flyburi.com',
'daum' : 'daum.net',
'naver' : 'naver.com'
}

print "buri's address is" , ab['buri']

del ab['buri']

print '\nThere are {} contacts in the address-book\n'.format(len(ab))

for name, address in ab.items():
	print 'Contact {} at {}'.format(name, address)

ab['test']='test.org'

if 'test' in ab:
	print "\ntest's address is", ab['test']
