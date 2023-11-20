a = int(input()) 
count = 0  # 화폐 개수를 세기 위한 변수수

for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:  # 사용 가능한 화폐를 for 문에 넣고
    if a // i != 0:  # a를 i로 나눈 몫이 0이 아니면
        count += a // i  # count에 a를 i로 나눈 몫을 추가
        a = a % i  # a 값을 a를 i로 나눈 나머지로 변경

print(count)  # count 값 출력하면 끝!!
