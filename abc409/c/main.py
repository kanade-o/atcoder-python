# 累積和の問題
n, l = map(int, input().split())

if l % 3 != 0:
  print(0)
  exit()

d = list(map(int, input().split()))
x = 0
cnt = [0]*l

# インデックス番号を座標とする
# その座標の出現回数を数える
for i in range(n):
  if i != 0:
    x += d[i-1]
  x %= l
  cnt[x] += 1

ans = 0
# 最初の点になりうるのは, 円周/3. //なのは奇数対策
for i in range(l // 3):
  # 掛け算にすることで, 存在しない点(0)が出てきたら0となる. 複数あっても一気に求めることができる
  # 三角形であるための条件は, x, x+l//3, x+2*l//3
  ans += cnt[i] * cnt[i+l//3] * cnt[i+2*l//3]
print(ans)