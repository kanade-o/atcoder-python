from sympy import factorint
N = int(input())
def div(num):
    factor=factorint(num)
    cnt=1
    for expon in factor.values():
        cnt*=(expon+1)
    return cnt

cnt = 0
for i in range(1, N+1):
  if div(i) == 9:
    cnt += 1

print(cnt)