num = int(input())
sum_of_evens = 0

for i in range(2, num+1, 2):
    sum_of_evens += i

print("{}".format(num, sum_of_evens))
