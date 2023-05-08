import sys

string_L = list(input()) #첫 문자열 입력 및 커서 왼쪽
string_R = [] # 커서 오른쪽
time = int(input()) #명령 횟수 입력
for i in range(time):
    command=sys.stdin.readline().split()
    if(command[0]=='L' and string_L):
        string_R.append(string_L.pop())
    elif(command[0]=='D' and string_R):
        string_L.append(string_R.pop())
    elif(command[0]=='B' and string_L):
        string_L.pop()
    elif(command[0]=='P'):
        string_L.append(command[1])       
print("".join(string_L + list(reversed(string_R)))) #reversed 함수는 iterator 객체로 변환되기 때문에 list로 변환