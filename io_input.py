def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

sth = raw_input("Enter text:")
if is_palindrome(sth):
	print "yes it is a palindrome"
else:
	print "no it is not a palindrome"

