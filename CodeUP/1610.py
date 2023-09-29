def mysubstr(string, start, count):
    return string[start:start+count]

input_str = input()  # 문자열 입력
start, count = map(int, input().split())  # 시작 위치와 글자 개수 입력

result = mysubstr(input_str, start, count)
print(result)

