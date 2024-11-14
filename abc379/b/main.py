N, K = map(int, input().split())
S = input()
split = S.split('X') 

ans = 0
for i in range(len(split)):
  if len(split[i]) >= K:
    ans += (len(split[i]) // K)
    
print(ans)