S = input()
X, Y = map(int, S.split('.'))

if 0 <= Y <= 2:
  print(f'{X}-')
elif 3 <= Y <= 6:
  print(f'{X}')
else:
  print(f'{X}+')
  