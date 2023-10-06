# readline을 사용하기 위해 import합니다.
from sys import stdin


# 길이 n을 입력합니다.
# 1 <= n <= 99
# int형으로 변환합니다.
n = int(stdin.readline())
# 입력한 길이 n에 대하여 숫자 피라미드에서 처음 시작하는 숫자를 계산하고 변수에 저장합니다.
# 처음 시작하는 숫자는 길이 n인 숫자 피라미드에서 숫자의 개수입니다.
start = n * (n + 1) // 2

# 입력한 길이 n만큼 반복해봅니다.
# 각 줄의 순서와 해당 줄에서 출력할 숫자의 개수를 의미하도록 1부터 n까지 반복합니다.
for line in range(1, n + 1):
    # 숫자 피라미드의 현재 줄에서 line만큼 반복해봅니다.
    for num in range(line):
        # 변수 start의 현재 값과 공백을 출력하고, 다음 줄로 내리지 않습니다.
        print(f'{start} ', end='')
        # 변수 start의 값에서 1을 빼고 다시 저장합니다.
        start -= 1
    # 숫자 피라미드에서 한 줄 출력이 끝나면 다음 줄로 넘어갑니다.
    print()
