import itertools
N, K = map(int, input().split())

time = []
for i in range(N):
  T = list(map(int, input().split()))
  time.append(T)

ans = 0
for root in itertools.permutations(range(1,N)):
  result_time = 0
  result_time += time[0][root[0]]
  current_city = root[0]
  
  for i in range(1, N-1):
    result_time += time[current_city][root[i]]
    current_city = root[i]
  
  result_time += time[current_city][0]
  
  if result_time == K:
    ans += 1

print(ans)