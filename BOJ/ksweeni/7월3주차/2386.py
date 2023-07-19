while True:
  arr = input().lower()
  if arr[0]=='#':
    break
  print(arr[0], arr.count(arr[0])-1)