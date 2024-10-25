N, S, D = map(int, input().split())

for i in range(N):
  x,y = map(int, input().split())
  if x<S and D<y:
    print("Yes")
    exit()

print("No")