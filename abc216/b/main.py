N = int(input())
S = []
T = []
for i in range(N):
  a, b = map(str, input().split())
  S.append(a)
  T.append(b)

for i in range(N):
  for j in range(i+1, N):
    if (S[i] == S[j]) and (T[i] == T[j]):
      print("Yes")
      exit()
print("No")