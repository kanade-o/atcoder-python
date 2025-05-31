n, m = map(int, input().split())
diff = [0]*(n+1)
for i in range(m):
  l, r = map(int, input().split())
  diff[l-1] += 1
  diff[r] -= 1 

ans = [0]*n
for i in range(0, n):
  if i == 0:
    ans[i] += diff[i]
  else:
    ans[i] += diff[i] + ans[i-1]
print(min(ans))