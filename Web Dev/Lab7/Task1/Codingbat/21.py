def string_match(a, b):
  cnt = 0
  n = min(len(a), len(b))
  for i in range(n-1):
    a1 = a[i:i+2]
    b1 = b[i:i+2]
    if a1 == b1: cnt+=1
  return cnt
