# ～競プロ体験1日目～

## [1問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0011&lang=jp) （１０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1/1-1.py)
```
w = int(input())
n = int(input())
map = [i for i in range(1, w+1)]
a = []
b = []
for i in range(n):
    x,y = input().split(",")
    a.append(int(x))
    b.append(int(y))
for i in range(w):
    for j in range(n-1,-1,-1):
        if map[i] == a[j]:
            map[i] = b[j]
        elif map[i] == b[j]:
            map[i] = a[j]
    print(map[i])
 ```

## [2問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0005&lang=jp) （１０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1/1-2.py)
```
import math
for i in range(50):
	try:
		data = input().split()
		a = int(data[0])
		b = int(data[1])
		print(math.gcd(a, b), int((a*b)/math.gcd(a, b))) 
	except:
		break
```

## [3問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0652) （１０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1/1-3.py)
```
data = input().split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
count = 1
coin = 0
while 1:
    coin += a
    if count % 7 == 0:
        coin += b
     
    if coin >= c:
        break
    else:
        count += 1
print(count)
```

## [4問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0022&lang=jp) （１５点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1/1-4.py)
```
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
```

## [5問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0100&lang=jp) （１５点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1/1-5.py)
```
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
```

## [6問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0004&lang=jp) （２０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1/1-.py)
```
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
```


[←back](https://7vxxi.github.io/my-portfolio/shin/1/)
