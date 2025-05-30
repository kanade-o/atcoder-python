n, y = map(int, input().split())
# 候補作成
kouho = []
for i in range(0, n+1):
  for j in range(0, n+1):
    for k in range(0, n+1):
      if (i+j+k) == n:
        kouho.append([i, j, k])

print(kouho)
# シミュレーション flag

# flagが立っていたらリストの中身を出力
# もしflagが立っていなかったら、-1を出力