'''
알파벳 대문자, 숫자 0~9로 구성된 문자열 입력
모든 알파벳을 오름차순 정렬 + 숫자 전부 더한 값 출력
K1KA5CB7 -> ABCKK13
'''

input_data = input()
result = []
value = 0

for x in input_data:
    if x.isalpha():  # 알파벳이면?
        result.append(x)
    else:  # 숫자면?
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))