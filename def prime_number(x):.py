def prime(x):
	for x in range (2,x):
		prime1 = True
	for i in range (2,x):
		if (x % i ==0):
			prime1 = False
	if prime1:
		prime1(x)
prime(50)