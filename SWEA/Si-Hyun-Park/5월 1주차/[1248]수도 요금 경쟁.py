T = int(input())

def a_comp(p, w) :
  return p*w
def b_comp(q, r, s, w) :
  if r >= w :
    return q
  else :
    return q+((w-r)*s)
for t in range(1, T+1) :
  p, q, r, s, w = map(int, input().split())
  print("#{} {}".format(t, min(a_comp(p, w), b_comp(q, r, s, w))))