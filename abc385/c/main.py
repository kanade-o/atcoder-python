N = int(input())
H = list(map(int, input().split()))
B = []
for i in range(N):
  standard = H[i]
  tmp = []
  for j in range(i+1,N):
    if H[i] == H[j]:
      tmp.append(H[j])
    else:
      tmp.append(' ')
  B.append(tmp)

for i in range(N):
  for j in range(N):
    