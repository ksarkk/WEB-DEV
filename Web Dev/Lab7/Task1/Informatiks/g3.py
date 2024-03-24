import math
n = int(input())
ok = False
for i in range(2, int(math.sqrt(n)) + 1):
  if n % i == 0:
    print(i)
    ok = True
    break
if ok == False: print(n)
