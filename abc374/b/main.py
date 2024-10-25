S = input()
T = input()

count = 1
flag = 0
for i in range(min(len(S), len(T))):
  if S[i] != T[i]:
    # count = i
    flag = 1
    break
  else :
    count += 1
    
if flag ==0 and len(S) == len(T):
  print(0)
else :
  print(count)