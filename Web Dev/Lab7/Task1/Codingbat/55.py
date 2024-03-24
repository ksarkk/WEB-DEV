def solve(n):
  if 13 <= n and n <= 19 and n != 15 and n!= 16:  return 0
  else: return n
  
def no_teen_sum(a, b, c):
  return solve(a) + solve(b) + solve(c)