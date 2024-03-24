def front_times(str, n):
  size=3
  if len(str)<3:
    size = len(str)
  s = str[:size]
  
  ans = ""
  for i in range(n):
    ans =ans + s
  return ans