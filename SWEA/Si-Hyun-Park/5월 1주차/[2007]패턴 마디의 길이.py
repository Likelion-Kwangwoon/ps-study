T = int(input())
for t in range(1, T + 1):
  s = input()
  ans = 0
  for i in range(1, len(s)):
    if s[:i] == s[i : 2 * i]:
      ans = i
      break

  print("#{} {}".format(t, ans))