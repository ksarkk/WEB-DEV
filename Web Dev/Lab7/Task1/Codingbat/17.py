def last2(str):
  if len(str) < 2:return 0
  lastTwo = str[len(str)-2:]
  cnt = 0
  for i in range(len(str)-2):
    s = str[i:i+2]
    if s == lastTwo:
      cnt+=1
  return cnt
