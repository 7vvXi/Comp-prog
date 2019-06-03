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
```
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
```

## [３問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0017&lang=jp) （１５点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/2/2-3.py)
```
while 1:
  try:
    str = input().split()
  except:
    break
  data = []
  for i in range(ord('a'), ord('z')+1):
    data.append(chr(i))
  tmp = []
  for i in range(len(str)):
    tmp.append(ord(str[i][0])-ord('t'))
  num = []
  for x in tmp:
    if x not in num:
      num.append(x)
  for i in range(len(num)):
    result = ""
    for j in range(len(str)):
      for ch in str[j]:
        if (ch == ',') or (ch == '.'):
          result += chr(ord(ch))
        elif (data.index(ch)-num[i]) > 25:
          result += data[data.index(ch)-num[i]-26]
        else:
          result += data[data.index(ch)-num[i]]
      result += " "
    if ('the' in result) or ('this' in result) or ('that' in result):
      break
  print(result[:-1])
```

## [４問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=3001) （２０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/2/2-4.py)
```
Wait a minute...
```

[←戻る](https://7vxxi.github.io/my-portfolio/shin/)
