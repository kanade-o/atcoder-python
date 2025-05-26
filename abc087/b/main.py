A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for five_hundred in range(0, A+1):
  for one_hundred in range(0, B+1):
    for fifty in range(0, C+1):
      num = (500*five_hundred) + (100*one_hundred) + (50*fifty)
      if num == X:
        ans += 1
print(ans)