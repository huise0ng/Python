n = int(input())  # 학생의 수 입력받기
scores = list(map(int, input().split()))  # 각 학생의 점수 입력받기

rankings = [1] * n  # 각 학생의 순위를 저장할 리스트 초기화

for i in range(n):
    for j in range(n):
        if scores[i] < scores[j]:  # i번째 학생보다 j번째 학생의 점수가 더 크면
            rankings[i] += 1  # i번째 학생의 순위 증가

# 입력된 순서대로 각 학생이 몇 등인지 출력
for k in range(n):
    print(scores[k], rankings[k])

