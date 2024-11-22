import re
N, K = map(int, input().split())
S = str(input())

result = re.findall(r'(0+|1+)', S)
address = 0
cnt = 0
for i in range(N):
  if '1' in result[i]:
    cnt += 1
    if cnt == K:
      address = i
      break
    
tmp = result[address-1]
result[address-1] = result[address]
result[address] = tmp

print("".join(result))
