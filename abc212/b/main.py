X = list(map(int, input()))
if X.count(X[1]) == 4:
  print('Weak')
  exit()

cnt = 0
for i in range(3):
  if (X[i]+1) % 10 == X[i+1]:
    cnt += 1

if cnt == 3:
  print('Weak')
  exit()


print('Strong')