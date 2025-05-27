n, a, b = map(int, input().split())

ans_list = []
for num in range(1, n+1):
  
  tmp = num
  count = 0
  # 各桁を出したいときは, 10でわると余りから得られる. 商は新たに割る対象とする.
  while True:
    if tmp == 0: break
    q, r = divmod(tmp, 10)
    count += r 
    tmp = q
  if a <= count <= b:
    ans_list.append(num)
print(sum(ans_list))