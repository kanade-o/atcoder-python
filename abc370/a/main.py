L, R = map(int, input().split())

if (L == 0 and R == 0) or (L == 1 and R == 1):
  print('Invalid')
  exit()

if L == 1 and R == 0:
  print('Yes')
else:
  print('No')