H, W, D = map(int, input().split())
S = []
for i in range(H):
  tmp = list(map(str, input()))
  S.append(tmp)

floor_list = []
for i in range(H):
  for j in range(W):
    if S[i][j] == '.':
      floor_list.append([i+1,j+1])

cnt_array = []
for i in range(len(floor_list)-1):
  x1 = floor_list[i][0]
  y1 = floor_list[i][1]
  cnt = 0
  for j in range(i+1, len(floor_list)):
    x2 = floor_list[j][0]
    y2 = floor_list[j][1]
    d = abs(x1-x2) + abs(y1-y2)
    if d <= D:
      cnt += 1
  cnt_array.append(cnt)

print(cnt_array)