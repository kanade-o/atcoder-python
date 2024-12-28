S = input()

count = 0
i = 0

while i < len(S):
  if S[i] == '0' and i + 1 < len(S) and S[i+1] == '0':
    count += 1
    i += 2
  else:
    count += 1
    i += 1
print(count)