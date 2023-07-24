m, n = map(int,input().split(' '))

if(len(str(m)) == n and str(n)[0]=='5'):
  print('1'+'0'*n)
else:
  print(round(m,-n))