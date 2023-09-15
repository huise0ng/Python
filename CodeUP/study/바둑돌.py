a = []

for i in range(19):
    a.append([])

    for j in range(19):
        a[i].append(0)

for i in range(19):
    a[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if a[x-1][j] == 0:
            a[x-1][j] = 1
        else:
            a[x-1][j] = 0
        if a[j][y-1] == 0:
            a[j][y-1] = 1
        else:
            a[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(a[i][j], end=" ")
    print()