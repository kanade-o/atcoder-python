matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = input()

for i in range(26):
  before = S.find(matrix[i])
  after = S.find(matrix[i+1])