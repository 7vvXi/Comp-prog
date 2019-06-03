# ～競プロ体験２日目～

## [1問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009&lang=jp) （１０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/2/2-1.py)
```
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
 ```

## [2問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0087) （１０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/2/2-2.py)


[←戻る](https://7vxxi.github.io/my-portfolio/shin/)
