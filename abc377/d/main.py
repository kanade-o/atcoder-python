N, M = map(int, input().split())
L = []
R = []
avoid = 0
for i in range(N):
  Li, Ri = map(int, input().split())
  for i in range(1, M+1):
    for j in range(i, M+1):
      if Li <= i and j <= Ri:
        avoid += 1
        

all = 0
for i in range(1, M+1):
  for j in range(i, M+1):
    all += 1
    
print(all - avoid)