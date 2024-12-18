S = input()
T = input()

if S == T:
  print("Yes")
  exit()

for i in range(len(S)-1):
  new_str = list(S)
  tmp = new_str[i]
  new_str[i] = new_str[i+1]
  new_str[i+1] = tmp
  if "".join(new_str) == T:
    print("Yes")
    exit()
print("No")