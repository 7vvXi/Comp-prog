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
