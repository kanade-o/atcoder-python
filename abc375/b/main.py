import math
n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

current_x = 0
current_y = 0
ans = 0
for i in range(n):
  new_x = x[i]
  new_y = y[i]
  ans += math.sqrt(pow(current_x-new_x, 2)+pow(current_y-new_y, 2))
  current_x = new_x
  current_y = new_y

ans += math.sqrt(pow(current_x, 2)+pow(current_y, 2))
print(ans)