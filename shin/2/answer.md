# ～競プロ体験２日目～

## [1問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009&lang=jp) （１０点）
#### [解答例](https://raw.githubusercontent.com/7vvXi/Comp-prog/master/shin/2/2-1.py)
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
#### [解答例](https://raw.githubusercontent.com/7vvXi/Comp-prog/master/shin/2/2-2.py)
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
#### [解答例](https://raw.githubusercontent.com/7vvXi/Comp-prog/master/shin/2/2-3.py)
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
#### [解答例](https://raw.githubusercontent.com/7vvXi/Comp-prog/master/shin/2/2-4.py)
```
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
```

## [５問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0086) （２５点）
#### [解答例](https://raw.githubusercontent.com/7vvXi/Comp-prog/master/shin/2/2-5.py)
```
Wait a minute...
```

## [EX](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_E&lang=jp) 
#### [解答例](https://raw.githubusercontent.com/7vvXi/Comp-prog/master/shin/2/ex.py)
```
str1 = input()
str2 = input()

dist = []

for i in range(len(str1)+1):
	dist.append([0]*(len(str2)+1))
	dist[i][0] = i
	
for j in range(len(str2)+1):
	dist[0][j] = j
	
calc = [0] * 3

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
        	calc[0] = dist[i-1][j-1]
        else:
        	calc[0] = dist[i-1][j-1] + 1
        	
        calc[1] = dist[i][j-1] + 1
        calc[2] = dist[i-1][j] + 1
        dist[i][j] = min(calc)
    
print(dist[len(str1)][len(str2)])
```
※どこかの試験で出た類題です。


[←戻る](https://7vxxi.github.io/Comp-prog/shin/)
