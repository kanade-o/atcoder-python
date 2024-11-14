S = int(input())

a = []
a.append(S)
for i in range(1000000):
  if a[i] % 2 == 0:
    value = a[i] / 2
  else:
    value = 3*a[i] + 1
  
  if(value in a):
    print(i+2)
    break
  
  a.append(value)