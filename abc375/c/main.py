import copy
N = int(input())
A = []
for i in range(N):
    row = list(input().strip())
    A.append(row)

ANS = copy.deepcopy(A)

for i in range(1, int(N/2)+1):
  for x in range(i, N+1-i):
    for y in range(i, N+1-i):
      if N+1-x < N:
        ANS[y][N+1-x] = A[x][y]


for row in ANS:
  print("".join(row))