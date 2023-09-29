# def r(n, a):
#   if n == 1: # n이 1이라면
#     a[1]=1 # 수행을 한 후 
#     return a[1] # a[1]을 리터어언
#   elif n==2: #n이 2라면
#     a[2] = 2 # 수행
#     return a[2] # a[2]도 리턴
#   elif n==3: #계속적인 반복 /  엔이 3이라면
#     a[3] = 4 # 또 값을 수행 
#     return a[3] # return a[3] 함니다.

#   if a[n]: 
#     return a[n]
#   else:
#     a[n] = (r(n-3, a)+r(n-2, a)+r(n-1, a)) % 1000
#     return a[n]
    
# n = int(input())
# a = [0 for _ in range(n+1)]
# print(r(n, a)) 


def r(n, a):
    if n == 1:
        a[1] = 1
        return a[1]
    elif n == 2:
        a[2] = 2
        return a[2]
    elif n == 3:
        a[3] = 4
        return a[3]

    if a[n]:
        return a[n]
    else:
        a[n] = (r(n - 3, a) + r(n - 2, a) + r(n - 1, a)) % 1000
        return a[n]


def recursive_r(n):
    if n <= 0:
      raise ValueError("n must be greater than zero.")

    # 일단 *아니고 배열 초기화
    arr = [0 for _ in range(n + 1)]
    
    # 재귀 함수 호출하는 부분임니다잇
    result = r(n, arr)
    
    return result


n = int(input())
print(recursive_r(n))
