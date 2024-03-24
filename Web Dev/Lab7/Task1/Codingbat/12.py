def front3(str):
  a = 3
  if len(str) < 3:
    a = len(str)
  s = str[:a]
  ans = s + s + s
  return ans