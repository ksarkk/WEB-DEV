def Xor(x, y):
    if x == 1 and y== 0: return 1
    elif x == 0 and y == 1: return 1
    else: return 0

a = list(map(int, input().split()))
for i in range(0, 2):
    print(Xor(a[i], a[i+1]))
    break
