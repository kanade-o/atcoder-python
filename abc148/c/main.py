def gcd(x: int, y: int) -> int:
  if y == 0:
    return x
  else:
    return gcd(y, x%y)

A, B = map(int, input().split())

ans = (A*B) / int(gcd(A, B))
print(int(ans))