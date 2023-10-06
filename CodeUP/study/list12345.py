def d(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + d(arr)

a = input().split()
for i in range(5):
    a[i] = int(a[i])

result = d(a)
print(result)
