# readline을 사용하기 위해 import합니다.
from sys import stdin


# 계단의 높이 n을 정수로 입력합니다.
# 1 <= n <= 100
# int형으로 변환합니다.
n = int(stdin.readline())

# 0부터 n-1까지 반복합니다.
for num in range(n):
    # 공백을 현재 숫자만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * num, end='')
    # 줄의 마지막에 **을 출력합니다.
    print('**')
