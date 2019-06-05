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
