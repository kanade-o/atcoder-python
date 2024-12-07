N = int(input())
S = input()

T = N

if N % 2 == 0:
  print("No")
  exit()
if S == '/':
  print('Yes')
  exit()

if S[int((T+1)/2)-1] != '/':
  print("No")
  exit()

for i in range(0,int((T+1)/2)-1):
  if S[i] != '1':
    print("No")
    exit()

for i in range(int((T+1)/2), T):
  if S[i] != '2':
    print("No")
    exit()

print("Yes")