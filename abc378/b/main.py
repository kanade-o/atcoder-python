N = int(input())
array_q = []
array_r = []
for i in range(N):
  q, r = map(int, input().split())
  array_q.append(q)
  array_r.append(r)
Q = int(input())
for i in range(Q):
  t, d = map(int, input().split())
  t -= 1
  b, c = divmod(d, array_q[t])
  a = 0
  if c <= array_r[t]:
    a = b
  else:
    a = b+1
  ans = a*array_q[t]+array_r[t]
  print(ans)

