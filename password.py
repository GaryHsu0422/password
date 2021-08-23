password = '123456'
c = 3
while True: 
	p = input('Please enter your password')
	if p == password: 
		print('your password is correct')
		break
	else: 
		c = c - 1
		print('Your password is incorrect, your still have', c ,'chances' )
		if c == 0:
			break
