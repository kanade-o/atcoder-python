K = int(input())
A, B = map(int, input().split())

def conv(num, K):
  ans = 0
  for i in str(num):
    ans *= K
    ans += int(i)
  return ans

ans = conv(A,K) * conv(B,K)
print(ans)