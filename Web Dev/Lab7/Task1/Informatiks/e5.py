n = int(input())
ok= 0
a = list(map(int, input().split()))
for i in range(0, n-1):
    if ((a[i]<0)and(a[i+1]<0))or((a[i]>0)and(a[i+1]>0)):
        ok=1
if ok == 1: print("YES")
else: print("NO")