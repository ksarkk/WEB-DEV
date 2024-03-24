n = int(input())
cnt= 0
a = list(map(int, input().split()))
for i in reversed(range(0, n)):
    print(a[i], end = " ")