K = int(input())
S = input()
T = input()

if abs(len(S) - len(T)) > 1:
  print("No")
  exit()

if len(S) == len(T):
  match_count = 0
  for i in range(len(S)):
    if S[i] == T[i]:
      match_count += 1
  if (len(S) - match_count) == 1 or (len(S) - match_count) == 0:
    print("Yes")
    exit()
  print("No")
  exit()
  
if len(S) > len(T):
  S, T = T, S
count = 0
while count < len(S) and S[count] == T[count]:
  count += 1
if T[:count] + T[count+1:] == S:
  print("Yes")
else:
  print("No")