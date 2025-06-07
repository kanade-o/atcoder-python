import collections
n = int(input())
a = list(map(int, input().split()))

ans = 0
a.sort(reverse=True)
for i in range(n):
  if a[i] >= i+1:
    ans = i+1
print(ans)