N, R = map(int, input().split())
T = R
for i in range(N):
  D, A = map(int, input().split())
  if D == 1:
    if 1600 <= T and T <= 2799:
      T += A
  elif D == 2:
    if 1200 <= T and T <= 2399:
      T += A
print(T)