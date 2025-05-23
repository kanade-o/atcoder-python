N, K = map(int, input().split())
array = list(map(int, input().split()))

value = 1
for item in array:
  value = value * item
  if len(str(value)) > K:
    value = 1

print(value)