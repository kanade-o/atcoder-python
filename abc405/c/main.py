# 表のように考える
# 求めたいのは, 要素番号が対象以外のところの面積を2で割ったところ(中央で対象なので)
# よって, (全面積 - 斜めの箇所の総和) / 2
n = int(input())
a = list(map(int, input().split()))

naname = 0
for i in range(0, n):
  naname += a[i]*a[i]

sum = 0
for i in range(0, n):
  sum += a[i]
ans = (sum*sum - naname) // 2 # floatだとエラーになるので, '//'整数除算(切り捨て)を使う
print(ans)