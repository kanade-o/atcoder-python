import itertools
S = list(input())

for v in itertools.permutations(S, len(S)):
  if "".join(v) == 'ABC':
    print("Yes")
    exit()

print("No")

