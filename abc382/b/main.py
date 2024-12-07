N , D = map(int, input().split())
S = list(input())
cnt = 0
for i in range(len(S)):
  if cnt >= D:
    break
  if S[int(len(S))-i-1] == '@':
    S[int(len(S))-i-1] = '.'
    cnt += 1

print("".join(S))