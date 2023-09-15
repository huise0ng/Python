sum=0
for x in range(0,11,2):d = []  # 빈 리스트 생성
for i in range(20):  # i가 0부터 19까지 반복
    d.append([])  # 빈 리스트를 d에 추가하여 2차원 리스트 생성
    for j in range(20):  # j가 0부터 19까지 반복
        d[i].append(0)  # 각 빈 리스트에 숫자 0을 추가하여 초기화

for i in range(19):  # i가 0부터 18까지 반복
    a = input().split()   # 입력받은 값을 공백을 기준으로 분리하여 a에 저장
    for j in range(19):   # j가 0부터 18까지 반복
        d[i + 1][j +1] = int(a[j])   # 분리된 값을 정수로 변환하여 해당 위치의 요소에 저장

n = int(input())   # 정수 n 입력받기

for i in range(n):   # n번 반복하는 동안 수행
    x, y = input().split()   # 좌표값 x와 y를 공백을 기준으로 분리하여 변수 x, y에 저장
    x = int(x)   # x를 정수로 변환
    y = int(y)   # y를 정수로 변환
    
    for j in range(1,20):   # j가 범위 [1,20)에서 반복하는 동안 수행
        
        if d[j][y] ==0:   
            d[j][y] =1     #(j,y) 위치의 값이 초기값인 경우 해당 위치의 값을 토글하기 위해 값을 변경함 
        else:
            d[j][y] =0     #(j,y) 위치의 값이 초기값이 아닌 경우 해당 위치의 값을 토글하기 위해 값을 변경함 

        if d[x][j] ==0:
            d[x][j] =1     #(x,j) 위치의 값이 초기값인 경우 해당 위치의 값을 토글하기 위해 값을 변경함 
        else:
            d[x][j]=0      #(x,j) 위치의 값이 초기값이 아닌 경우 해당 위치의 값을 토글하기 위해 

for i in range(1,20):
    
    for j in range (1,20):
        
        print(d[i][j], end=' ')  
        
    print()

    sum+=x
    print(x,end=" ")
print(" ")
print(" ", sum)