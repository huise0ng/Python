def recursive_pop_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + recursive_pop_sum(arr)

a = input().split()
for i in range(5):
    a[i] = int(a[i])

result = recursive_pop_sum(a)
print(result)
