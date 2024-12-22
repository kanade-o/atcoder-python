A, B, C = map(int, input().split())

if A == B == C:
  print("Yes")
  exit()


if (A+B) == C:
  print("Yes")
  exit()
elif (B+C) == A:
  print("Yes")
  exit()
elif (A+C) == B:
  print("Yes")
  exit()
print("No")