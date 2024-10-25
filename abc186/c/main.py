def judge_ten(x: int) -> bool:
  x = str(x)
  if "7" in x:
    return True
  else:
    return False

def judge_eight(x: int) -> bool:
  s = ""
  while x>0:
    s = str(x%8) + s
    x //= 8
  if "7" in s:
    return True
  else:
    return False

N = int(input())
ans = 0
for i in range(1, N+1):
  if not judge_eight(i) and not judge_ten(i):
    ans += 1
print(ans)