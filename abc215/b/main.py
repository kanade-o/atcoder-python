N = int(input())
num = 1
for k in range(60+1):
  if num > N:
    print(k-1)
    exit()
  num *= 2