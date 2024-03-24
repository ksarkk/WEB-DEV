def front_back(str):
  if len(str) <= 1: return str
  mid = str[1:-1] 
  ans = str[len(str)-1] + mid + str[0]
  return ans
