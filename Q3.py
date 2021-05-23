n = int(input())
if n < 9:
	print("Invalid Input")
else:
	even_factors = []
	prime = True
	for i in range(n+1, 1, -1):
		if n % i == 0:
			if(i != n):
				prime = False
			if i % 2 == 0:
				even_factors.append(i);
	if prime: 
		print("Please input a different number")
	else:
		print(even_factors)