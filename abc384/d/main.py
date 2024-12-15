N, S = map(int, input().split())
A = list(map(int, input().split()))

num = 0
for i in range(N):
  num += A[i]

sum = 0
while (sum <= S):
  sum += num
  if sum == S:
    print("Yes")
    exit()
print("No")