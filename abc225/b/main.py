N = int(input())
count = [0] * N
for _ in range(N-1):
  a, b = map(int, input().split())
  count[a-1] += 1
  count[b-1] += 1

isStar = False
for i in range(N):
  if count[i] == (N-1):
    isStar = True
    
if isStar:
  print("Yes")
else:
  print("No")