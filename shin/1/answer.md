# ～競プロ体験1日目～

### [1問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0011&lang=jp) （１０点）
#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1-1.py)
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

### [2問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0005&lang=jp) （１０点）
>http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0005&lang=jp

#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1-2.py)
>https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1-2.py

### [3問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0022&lang=jp) （２０点）
>http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0022&lang=jp

#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1-3.py)
>https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1-3.py

### [4問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0004&lang=jp) （２０点）
>http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0004&lang=jp

### [5問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0100&lang=jp) （３０点）
>http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0100&lang=jp

### [6問目](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0652) （３０点）
>http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0652

#### [解答例](https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1-6.py)
>https://raw.githubusercontent.com/7vXXi/my-portfolio/master/shin/1-3.py

※コンパイルしてから提出してください。一回WAするたびに-1点します。
