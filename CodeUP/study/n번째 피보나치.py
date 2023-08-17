def func(n):
    if n==0:
        result = 1
    elif n==1:
        result = 1
    else:
        result = func(n-1) + func(n-2)
    return result

n = 5

print(n+1,func(n))