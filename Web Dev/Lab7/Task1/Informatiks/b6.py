def power(a, n):
    return a**n

a = list(map(int, input().split()))
for i in range (0, 2):
    print(power(a[i], a[i+1]))
    break
