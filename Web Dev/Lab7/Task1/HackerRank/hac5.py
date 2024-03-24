# Lists
if __name__ == '__main__':
    N = int(input())
    ar = list()

    for i in range(N):
        a = input().split()
        if a[0] == "print":
            print(ar)
        elif a[0] == "insert":
            ar.insert(int(a[1]), int(a[2]))
        elif a[0] == "remove":
            ar.remove(int(a[1]))
        elif a[0] == "append":
            ar.append(int(a[1]))
        elif a[0] == "sort":
            ar = sorted(ar)
        elif a[0] == "pop":
            ar.pop()
        elif a[0] == "reverse":
            ar.reverse()