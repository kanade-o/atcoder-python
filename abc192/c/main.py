def g1(x: int) -> int:
  x = list(str(x))
  x.sort(reverse=True)
  x="".join(x)
  return int(x)

def g2(x: int) -> int:
  x = list(str(x))
  x.sort()
  x="".join(x)
  return int(x)

def f(x: int) -> int:
  return g1(x) - g2(x)

N, K = map(int, input().split())
ans = N
for i in range(K):
  ans = f(ans)
print(ans)