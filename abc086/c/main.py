# まず時間の差よりも距離が大きかったら弾く
# 時間差と距離はお互いに偶数であるか奇数であるかという必要がある
# 更新忘れずに
n = int(input())
array = []
for _ in range(n):
  t, x, y = map(int, input().split())
  array.append([t, x, y])

pre_time = 0
pre_x = 0
pre_y = 0
can = True
for i in range(n):
  current_time = array[i][0]
  current_x = array[i][1]
  current_y = array[i][2]

  sub_time = current_time - pre_time
  distance = abs(current_x - pre_x) + abs(current_y - pre_y)

  if sub_time < distance:
    can = False
  if (distance % 2 != sub_time % 2):
    can = False
  
  pre_time = current_time
  pre_x = current_x
  pre_y = current_y
  
if can:
  print("Yes")
else:
  print("No")