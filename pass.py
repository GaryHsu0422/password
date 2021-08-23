password = '123456'
c = 3
while c > 0: 
	c = c - 1
	p = input('Please enter your password: ')
	if p == password: 
		print('your password is correct')
		break
	else: 
		print('Your password is incorrect')
		if c > 0: 
			print('you still have', c, 'chances')
