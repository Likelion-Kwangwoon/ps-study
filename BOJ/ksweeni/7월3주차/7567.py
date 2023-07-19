plate = input()
answer = 10
for i in range(1,len(plate)):
  if plate[i] == plate[i-1]:
    answer += 5
  else:
    answer+=10
print(answer)