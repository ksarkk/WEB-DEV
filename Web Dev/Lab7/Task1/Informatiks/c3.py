import math
a = int(input())
b = int(input()) + 1
for i in range(a, b):
    if int(math.sqrt(i)) == math.sqrt(i): print(i)