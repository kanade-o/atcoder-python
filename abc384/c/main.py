array = list(map(int, input().split()))

import itertools
for i in range(1, 5+1):
  for comb in itertools.combinations("ABCDE", i):
    print(comb)