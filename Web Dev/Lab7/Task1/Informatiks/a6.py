def mini(a, b, c, d):
    m=a
    if (b<m):  m=b
    if (c<m):  m=c
    if (d<m):  m=d
    return m

a = list(map(int, input().split()))
for i in range(0, 4):
    print(mini(a[i], a[i+1], a[i+2], a[i+3]))
    break

