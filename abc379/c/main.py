N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

#N - X[N] + 1 > A[N]
if N - X[M-1] +1 < A[M-1]:
  print(-1)
  exit()

ans = 0
for i in range(M):
  ans += (A[i]*(A[i]-1)) // 2
print(int(ans))
