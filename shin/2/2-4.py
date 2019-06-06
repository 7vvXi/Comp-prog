n = int(input())

data = [0] * 100001
draw = [0] * 4001
win = [0] * 4001

for i in range(n):
	data[i] = float(input())
	in_data = data[i] * 1000 + 0.0001
	in_data = int(in_data)
	draw[in_data] += 1
sum = n
for i in range(4000, 0, -1):
	sum -= draw[i]
	win[i] = sum
for i in range(n):
	out_data = data[i] * 1000 + 0.0001
	out_data = int(out_data)
	if draw[out_data] <= 1:
		print(win[out_data]*3)
	else:
		print(win[out_data]*3 + draw[out_data] - 1)
