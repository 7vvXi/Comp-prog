data = [1] * 1000000
i = 3
while i * i < 1000000:
    for j in range(3 * i, 1000000, 2 * i):
    	data[j] = 0
    i += 2

while 1:
	try:
		n = int(input())
	except:
		break
	count = 1
	if n <= 1:
		count = 0
	if n > 2:
		for i in range(3, n+1, 2):
			if data[i] == 1:
				count += 1
	print(count)
