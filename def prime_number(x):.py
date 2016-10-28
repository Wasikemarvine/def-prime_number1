def prime(y):
	for x in range (2,y):
		prime1 = True
	for i in range (2,y):
		if (y % i ==0):
			prime1 = False
	if prime1:
		prime1(y)
prime(50)