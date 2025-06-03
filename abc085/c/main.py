n, y = map(int, input().split())
# 3重ループだと計算量が多いので, 2重にして3つ目は式で求める.
# kが取りうる値がマイナスに行ってしまう点に注意
kouho = []
for i in range(0, n+1):
  for j in range(0, n+1):
    k = n - (i+j)
    money = 10000*i + 5000*j + 1000*k
    if k >= 0:
      if (money) == y:
        print(f'{i} {j} {k}')
        exit()

print("-1 -1 -1")