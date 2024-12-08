N = int(input())

water = 0
old_time = 0
for i in range(N):
  t, v = map(int, input().split())
  water -= t - old_time
  old_time = t
  if water < 0:
    water = 0
  water += v

print(water)