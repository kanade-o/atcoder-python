n = int(input())

d = []
for i in range(n):
  num = int(input())
  d.append(num)

d = sorted(d, reverse=True)
ans = 0
array = []
for num in d:
  if not array:
    ans += 1
    array.append(num)
  
  if num < array[len(array)-1]:
    ans += 1
    array.append(num)
print(ans)
