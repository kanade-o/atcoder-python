S, T = map(int, input().split())
cnt = 0
for a in range(100+1):
  for b in range(100+1):
    for c in range(100+1):
      if (a+b+c) <= S and (a*b*c) <= T:
        cnt += 1
print(cnt)