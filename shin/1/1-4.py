while 1:
	n = int(input())
	if n == 0:
		break
	a = [0] * 5001
	for i in range(n):
		a[i] = int(input())
	max = a[0]
	for i in range(n):
		sum = 0
		for j in range(i, n):
			sum += a[j]
			if sum >= max:
				max = sum
		
	print(max)
