n=int(input())
op=list(input())
num=[int(input()) for i in range(n)]

st = []

for i in op:
  if i.isalpha():
    st.append(num[ord(i)-65])
  else:
    x = st.pop()
    res = st.pop()
    if i == '+':
      res+=x
    elif i == '-':
      res-=x
    elif i == '*':
      res*=x
    elif i == '/':
      res/=x
    st.append(res)
    
print('%.2f' %st[-1])