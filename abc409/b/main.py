n = int(input())
a = list(map(int, input().split()))
# 最大を求めたいときは, 後ろから見ていくと計算回数を削減できる:w:w
for x in range(n, -1, -1):
  count = 0
  for val in a:
    if val >= x:
      count += 1
  if count >= x:
    print(x)
    break