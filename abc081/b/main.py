n = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
  is_all_even = True
  for i in a:
    if i % 2 == 1:
      is_all_even = False
  
  if is_all_even:
    ans += 1
    for i in range(len(a)):
      a[i] = a[i] / 2
  else:
    print(ans)
    exit()