N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
  A[i] -= 1

ans = 0
while True:
  exists = [False] * M
  for i in A:
    exists[i] = True

  ok = False
  for i in exists:
    if not i:
      ok = True
  if ok:
    break
  ans += 1
  A.pop()
print(ans)