N = int(input())
q = []
r = []
for i in range(N):
  qi, ri = map(int, input().split())
  q.append(qi)
  r.append(ri)

Q = int(input())
for i in range(Q):
  t, d = map(int, input().split())
  ans = d 