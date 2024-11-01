grid = [list(input().strip()) for _ in range(8)]

rows = set()
cols = set()
for i in range(8):
  for j in range(8):
    if grid[i][j] == '#':
      rows.add(i)
      cols.add(j)

for i in range(8):
  for j in range(8):
    if i in rows or j in cols:
      grid[i][j] = '#'
      

taken = 0
for i in range(8):
  for j in range(8):
    if grid[i][j] == '#':
      taken += 1
      
ans = 64 - taken
print(ans)