P = list(map(int, input().split()))
qwerty = list("abcdefghijklmnopqrstuvwxyz")
ans = ''
for i in range(len(P)):
  ans += qwerty[P[i]-1]
print(ans)