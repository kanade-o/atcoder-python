Q = int(input())

query = []
for i in range(Q):
    inputs = input().split()
    index = int(inputs[0])
    if len(inputs) > 1:
        para = int(inputs[1])
        query.append([index, para])
    else:
        query.append([index])

plant = []
for i in range(Q):
  if query[i][0] == 1:
    plant.append(0)
  elif query[i][0] == 2:
    plant = [num + query[i][1] for num in plant]
  elif query[i][0] == 3:
    cnt = 0
    for j in plant:
      if j >= query[i][1]:
        cnt += 1
    plant = list(filter(lambda x: x < query[i][1], plant))
    print(cnt)
