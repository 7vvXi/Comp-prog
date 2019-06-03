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
