n = int(input())
cnt= 0
a = list(map(int, input().split()))
for i in range(1, n):
   if a[i]>a[i-1]: 
     cnt+=1
print(cnt)