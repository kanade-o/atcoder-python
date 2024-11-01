N, C = map(int, input().split())
T = list(map(int, input().split()))

ans = 1
now_sec = T[0]
for i in range(1,N): 
  if T[i] - now_sec >= C:
    ans += 1
    now_sec = T[i]

print(ans)