n, x = map(int, input().split())

alcohol = 0
for i in range(n):
  v, p = map(int, input().split())
  alcohol += v*p
  if 100*x < alcohol:
    print(i+1)
    exit()
    
print(-1)

