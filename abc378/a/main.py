A = list(map(int, input().split()))
count = 0
for num in range(1, 5):
  count += A.count(num) // 2
    
print(count)