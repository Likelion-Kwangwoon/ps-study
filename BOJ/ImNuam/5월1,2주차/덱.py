import sys
class deq:
    front=0
    rear=0
    max_length=10000
    arr=[]
    def __init__(self):
        self.arr=[-1 for i in range(self.max_length)]
    def push_front(self, data):
        self.arr[self.front]=data
        self.front = (self.front-1+self.max_length)%self.max_length
    def push_back(self, data):
        self.rear = (self.rear+1)%self.max_length
        self.arr[self.rear]=data
    def pop_front(self):
        if self.rear==self.front:
            return -1
        self.front=(self.front+1)%self.max_length
        return self.arr[self.front]
    def pop_back(self):
        if self.rear==self.front:
            return -1
        tmp=self.rear
        self.rear=(self.rear-1+self.max_length)%self.max_length
        return self.arr[tmp]
    def empty(self):
        if self.rear==self.front:
            return 1
        else: return 0
    def size(self):
        return (self.rear-self.front)%self.max_length
    def first(self):
        if self.rear==self.front:
            return -1
        tmp = (self.front+1)%self.max_length
        return self.arr[tmp]
    def back(self):
        if self.rear==self.front:
            return -1
        return self.arr[self.rear]
cnt = int(input())
deque = deq()
for i in range(cnt):    
    command=sys.stdin.readline().split()
    if command[0] == "push_back":
        deque.push_back(command[1])
    elif command[0] == "push_front":
        deque.push_front(command[1])
    elif command[0] == "front":
        print(deque.first())
    elif command[0] == "back":
        print(deque.back())
    elif command[0] == "pop_back":
        print(deque.pop_back())
    elif command[0] == "pop_front":
        print(deque.pop_front())
    elif command[0] == "size":
        print(deque.size())
    elif command[0] == "empty":
        print(deque.empty())
    