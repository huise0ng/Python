n = int(input())
a = list(map(int, input().split()))  # 입력 받은 값을 정수로 변환하여 리스트에 저장

d = [0] * 24  # 리스트 초기화

# 컴프리헨션을 사용하여 d 리스트 갱신
[d.__setitem__(i, a.count(i)) for i in range(24)]

# 결과 출력
print(*d[1:])
