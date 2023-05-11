import sys
class deque:
    def __init__(self, length):
        self.front=0
        self.rear=length
        self.deq=[0 for i in range(length)]
    def del_rear(self):
        self.rear-=1
    def del_front(self):
        self.front+=1
count = int(input())
for i in range(count):
    command=list(input())
    arr_length=int(input())
    not_parsed_arr=input()
    reverse=False
    check_for_break=False
    
    arr=deque(arr_length)
    not_parsed_arr=not_parsed_arr[1:len(not_parsed_arr)-1]
    if arr_length!=0:
        arr.deq=list(map(int, not_parsed_arr.split(',')))
    else:
        arr.deq=[]
    if arr_length!=len(arr.deq):
        print("error")
        check_for_break=True
        break
    for j in range(len(command)):
        if command[j]=='R':
            reverse = not reverse
        if command[j]=='D':
            if arr.rear<=arr.front:
                print("error")
                check_for_break=True
                break
            elif reverse:
                arr.del_rear()
            else:
                arr.del_front()
    string="["
    arr_now_length=arr.rear-arr.front
    if not check_for_break:
        for w in range(arr_now_length):
            if not reverse:
                if w==0:
                    string = string+str(arr.deq[w+arr.front])
                else:
                    string=string+','+str(arr.deq[w+arr.front])
            else:
                if w==0:
                    string= string + str(arr.deq[arr.rear-w-1])
                else:
                    string=string+','+str(arr.deq[arr.rear-w-1])
        string=string+']'
        print(string)