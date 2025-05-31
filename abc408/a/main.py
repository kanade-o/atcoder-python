n, s = map(int, input().split())
t = list(map(int, input().split()))

last_time = 0
for time in t:
  if time - last_time <= s:
    last_time = time
  else:
    print("No")
    exit()
print("Yes")