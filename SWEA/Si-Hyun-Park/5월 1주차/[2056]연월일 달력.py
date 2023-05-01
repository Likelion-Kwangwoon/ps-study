T = int(input())

for i in range(1, T + 1):
  date = int(input())
  year = date // 10000
  month = (date % 10000) // 100
  day = date % 100
  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if (1 <= month <= 12) :
    if (1 <= date % 100 <= days[month-1]) :
      print("#{} {}/{}/{}".format(i, format(year,'04'), format(month,'02'), format(day,'02')))
    else : print("#{} -1". format(i))
  else : print("#{} -1". format(i))