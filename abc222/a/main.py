N = list(input())
if len(N) == 4:
  print("".join(N))
else:
  ans = ''
  for i in range(4-len(N)):
    ans += '0'
  ans += "".join(N)
  print(ans)

