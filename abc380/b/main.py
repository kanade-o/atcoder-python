S = input()
S = S.split('|')

array = []
for i in range(len(S)):
  if '-' in S[i]:
    num = S[i].count('-')
    array.append(num)

print(*array)