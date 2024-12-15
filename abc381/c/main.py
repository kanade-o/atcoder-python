N = int(input())
S = input()
ans = 0
for i in range(N):
  if S[i] != '/': continue
  d = 0
  while(True):
    l = i - (d+1)
    r = i + (d+1)
    if not 0 <= l < N: break
    if not 0 <= r < N: break
    if S[l] != '1': break
    if S[r] != '2': break
    d += 1
  ans = max(ans, 1+d*2)
print(ans)