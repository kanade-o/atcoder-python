# !/usr/bin/env python3
A, B, C, D = map(int, input().split())
if A < C:
  print("No")
elif A > C:
  print("Yes")
elif A == C and B < D:
  print("No")
else:
  print("Yes")