while 1:
	try:
		a1,b1,c1,a2,b2,c2 = list(map(float, input().split()))
	except:
		break
	A = a1 * b2 - b1 * a2
	x = (c1 * b2 - b1 * c2) / A
	y = (a1 * c2 - c1 * a2) / A
	if abs(x) <= 0.0001:
		x = 0.000
	if abs(y) <= 0.0001:
		y = 0.000
	print('{:.3f} {:.3f}'.format(x, y))
