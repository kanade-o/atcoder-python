N, Q = map(int, input().split())
query = []
for i in range(Q):
  H, T = map(int, input().split())
  H = str(H)
  query.append([H, T])

current_R = 1
current_L = 2

for i in range(Q):
  if query[i][0] == 'R':
    