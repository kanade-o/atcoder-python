S = list(input())
if S.count(S[0]) == 3:
  print(1)
elif S.count(S[0]) == 2 or S.count(S[1]) == 2:
  print(3)
else:
  print(6)