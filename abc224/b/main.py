H, W = map(int, input().split())
A = []
for _ in range(H):
  A.append(list(map(int, input().split())))

for i_1 in range(H):
  for i_2 in range(i_1+1, H):
    for j_1 in range(W):
      for j_2 in range(j_1+1, W):
        if (A[i_1][j_1] + A[i_2][j_2] > A[i_1][j_2] + A[i_2][j_1]):
          print("No")
          exit()
print("Yes")