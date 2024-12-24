N = int(input())
A = list(map(int, input().split()))
last = {}
B = [-1] * N
for i in range(N):
  if A[i] in last:
    B[i] = last[A[i]]
  last[A[i]] = i + 1
print(*B)