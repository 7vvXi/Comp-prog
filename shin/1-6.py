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
