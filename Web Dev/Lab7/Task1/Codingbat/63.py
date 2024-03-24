def count_hi(str):
  cnt = 0
  for i in range(len(str)-1):
    cnt += str[i:i+2] == 'hi'
  return cnt
