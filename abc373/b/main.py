matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = input()

count = 0
for i in range(25):
  before = S.find(matrix[i])
  after = S.find(matrix[i+1])
  count += abs(after - before)
print(count)