from collections import Counter
A, B, C, D = map(int, input().split())

counts = Counter([A, B, C, D])
values = list(counts.values())

if (3 in values and 1 in values) or (2 in values and values.count(2) == 2):
    print("Yes")
else:
    print("No")