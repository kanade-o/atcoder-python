n = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

for turn in range(len(a)):
  if turn % 2 == 0:
    alice += max(a)
    a.remove(max(a))
  else:
    bob += max(a)
    a.remove(max(a))
print(alice-bob)