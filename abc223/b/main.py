S = input()
n = len(S)
array = []
for i in range(0, n):
  array.append(S[i:n] + S[0:i])
print(min(array))
print(max(array))
