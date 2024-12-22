H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = []
for _ in range(H):
  a = list(input())
  S.append(a)

T = list(input())
houses = set()


for i in range(len(T)):
    # print(X,Y)
    if T[i] == 'U' and (S[X-1][Y] == '.' or S[X-1][Y] == '@'):
      if S[X-1][Y] == '@':
        houses.add((X-1, Y))
      X = X-1
      Y = Y
    elif T[i] == 'D' and (S[X+1][Y] == '.' or S[X+1][Y] == '@'):
      if S[X+1][Y] == '@':
        houses.add((X+1, Y))
      X = X+1
      Y = Y
    elif T[i] == 'L' and (S[X][Y-1] == '.' or S[X][Y-1] == '@'):
      if S[X][Y-1] == '@':
        houses.add((X, Y-1))
      X = X
      Y = Y-1
    elif T[i] == 'R' and (S[X][Y+1] == '.' or S[X][Y+1] == '@'):
      if S[X][Y+1] == '@':
        houses.add((X, Y+1))
      X = X
      Y = Y+1
    else:
      X = X
      Y = Y
print(f'{X+1} {Y+1} {len(houses)}')