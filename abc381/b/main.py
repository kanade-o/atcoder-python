S = input()
T = len(S)

if T % 2 != 0:
  print("No")
  exit()
  
for i in range(0, int(T/2)-1):
  if S[2*i] != S[2*i+1]:
    print("No")
    exit()
    
for i in range(0,T,2):
  if S.count(S[i]) != 2:
    print('No')
    exit()

print("Yes")