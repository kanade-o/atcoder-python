N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
ans = 0
a_sum = sum(A)
for i in range(N):
  a_sum -= A[i]
  ans += A[i]*(a_sum)
    
print(ans % mod)