while 1:
	try:
		line = input().split()
	except:
		break
	data = []
	for i in range(len(line)):
		try:
			data.append(float(line[i]))
		except:
			prev1 = data.pop(-1)#1つ前
			prev2 = data.pop(-1)#2つ前
			if line[i] == '+':
				result = prev2 + prev1
			elif line[i] == '-':
				result = prev2 - prev1
			elif line[i] == '*':
				result = prev2 * prev1
			elif line[i] == '/':
				result = prev2 / prev1
			data.append(result)
	print('{0:6f}'.format(data.pop(-1)))
