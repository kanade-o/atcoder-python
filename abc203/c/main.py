N, K = map(int, input().split())

friends = []
for i in range(N):
  A, B = map(int, input().split())
  friends.append([A, B])
friends.sort()

current_village = 0
current_village += K

for i in range(N):
  friend_village = friends[i][0]
  friend_money = friends[i][1]
  if friend_village <= current_village:
    current_village += friend_money
  else:
    break

print(current_village)