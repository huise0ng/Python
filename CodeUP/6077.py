n = int(input())
count = 0

for i in range(n+1):
    if (i % 2 == 0):
        count = count + i
    
    else:
        continue
    
print(count)