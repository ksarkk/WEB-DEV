n = int(input())
cnt = 0
a = list(map(int, input().split()))
for i in range(0, n):
   if a[i] > 0: cnt+=1
print(cnt)