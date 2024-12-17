N, Q = map(int, input().split())
S = list(input())
L = [ None ] * Q
R = [ None ] * Q

ok = [0] * (N-1)
for i in range(N-1):
  if S[i] == 'A' and S[i+1] == 'C':
    ok[i] = 1

sm = [0] * (N-1)
sm[0] = ok[0]
for i in range(N-1):
  sm[i] = sm[i-1] + ok[i]

for _ in range(Q):
  L, R = map(int, input().split())
  L -= 1
  R -= 1

  ans = sm[R - 1]
  if L > 0:
    ans -= sm[L - 1]

  print(ans)