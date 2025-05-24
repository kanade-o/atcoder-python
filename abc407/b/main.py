import itertools
from decimal import Decimal, getcontext, ROUND_HALF_UP

x, y = map(int, input().split())
getcontext().prec = 50
all_rolls = list(itertools.product(range(1, 7), repeat=2))

ans_list = set()
count = 0
for a, b in all_rolls:
  if ((a+b) >= x) or (abs(a-b) >= y):
    count += 1
    ans_list.add((a,b))
#   # if a + b >= x:
#   #   ans_list.add((a,b))
#   # if abs(a-b) >= y:
#   #   ans_list.add((a,b))

ans = Decimal(count) / Decimal(len(all_rolls))
print(f"{ans}")