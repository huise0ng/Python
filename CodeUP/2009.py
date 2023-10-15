k, n = map(int, input().split())  # 쿠폰 개수(k)와 필요 쿠폰 개수(n) 입력받기
c = 0  # 아메리카노 개수 초기화

while k >= n:
    tmp = k // n  # 쿠폰으로 먹을 수 있는 잔
    k -= tmp * n  # 현재 쿠폰 - 사용한 쿠폰
    k += tmp  # 현재 쿠폰 + 먹어서 생긴 쿠폰
    c += tmp

print(c)

