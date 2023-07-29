# a = "Life is too short, You need Python"
# print(a[2])

# 0,1,2 순으로 시작한다. 위의 글을 본다면 0은 L 1은 i 가 된다.

# a = "20010331Rainy"
# print(a[2:8])

# a[이상 : 미만 : 간격] 
# -를 붙이면 뒤에서부터 시작

# a = "I eat %d apples." % 3
# print(a)

# %d를 넣으면 뒤에 있는 %3의 3이 d에 들어간다.

# umber = 10
# day = "three"
# a = "I ate %d apples. so I was sick for %s days." % (number, day)
# print(a)

# a = "%10s" % "hi"
# print(a)

# 10칸이 띄워지고 hi가 나온다.

# a = "hobby"
# print(a.count('b'))

# a에서 b의 개수를 알려준다. find함수를 쓰게되면 b가 어디에 있는지 위치를 알려준다.

# lower 함수는 대문자를 소문자로 바꾸어준다. HI -> hi // a.lower()
# stirp 공백을 지운다. // a.srtip()
# upper 함수는 소문자를 대문자로 바꾸어 준다. hi -> HI // a.upper()

# a = "Life is too short"
# print(a.replace("Life", "Your leg"))

# repalce 함수는 Life라는 내용을 Your leg로 바꿔준다.

# a = "Life is too short"
# print(a.split())

# 문자열 자료형이 있으면 띄어쓰기 기준으로 자르는 함수인 split


#리스트
# a = ["이시영","문재성","int","신희성"]
# print(a)

#리스트 안에 리스트를 넣을 수도 있다.

# a = [1, 2, 3]
# b = [4 ,5 ,6]
# print(a + b)

#리스트 끼리 서로 더할 수도 있다.

# a = ["박주하","잠수","문재성"]
# a.append("시우버")
# print(a)

# append는 더한다는 뜻을 가지고 있고, append 함수를 사용하면 리스트에 요소를 추가할 수 있다.
# reverse 함수를 쓰면 리스트를 뒤집을 수도 있다.
# insert 함수는 특정 인덱스에 내용을 삽입할 수 있다. 
# remove 값을 제거할 수 있다. 
# pop 함수는 리스트에서 마지막 것이 튀어나간다.
# count 함수는 리스트에 있는 X의 개수를 새어준다.
# extend 함수는 리스트를 추가할 수 있다.