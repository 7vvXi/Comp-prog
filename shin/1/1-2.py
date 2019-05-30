import math

for i in range(50):
	try:
		data = input().split()
		a = int(data[0])
		b = int(data[1])
		print(math.gcd(a, b), int((a*b)/math.gcd(a, b))) 
	except:
		break
