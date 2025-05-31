n = int(input())
a = list(map(int, input().split()))

ans = set()
for num in a:
  ans.add(num)

ans = sorted(list(ans))
print(len(ans))
print(*ans)