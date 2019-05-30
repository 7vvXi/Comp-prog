while 1:
	n = int(input())
	if n <= 0:
		break
	name = []
	money = [0] * 4001
	for i in range(n):
		data = input().split()
		num = int(data[0])
		sum = int(data[1]) * int(data[2])
		if money[num] <= 0:
			name.append(num)
			money[num] = sum
		else:
			money[num] += sum
	flag = True
	for id in name:
		if money[id] >= 1000000:
			print(id)
			flag = False
	if flag:
		print('NA')
