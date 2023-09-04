def func(n):
    if n==0:   # n==0 이라면 결과갑을 1로 반환
        result = 1
    elif n==1: #n==1 이라면 결과값을 1로 반환
        result = 1
    else:
        result = func(n-1) + func(n-2)
    return result

n = 5

print(n+1,func(n))