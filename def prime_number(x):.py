def prime_number(x):
	for x in range (2,x):
		prime = True
	for i in range (2,x):
		if (x % i ==0):
			prime = False
	if prime:
		prime(x)
prime_number(23)