N = int(input())
P = list(map(int, input().split()))


def count_tilde(P):
  # 符号化
  B = []
  for i in range(N-1):
    if P[i] < P[i+1]:
      B.append(1)
    else:
      B.append(-1)

  # 符号をまとめる == 符号が変わる点を扱いやすくする
  runs = []
  cur_sign = B[0]
  cur_len = 1
  for x in B[1:]:
    if x == cur_sign:
      cur_len +=1
    else:
      runs.append((cur_sign, cur_len))
      cur_sign = x 
      cur_len = 1
  runs.append((cur_sign, cur_len))
  
  total = 0
  for i in range(len(runs)-2):
    s1, len1 = runs[i]
    s2, _ = runs[i+1]
    s3, len3 = runs[i+2]
    if (s1 == 1) and (s2 == -1) and (s3 == 1):
      total += len1 * len3
  
  return(total)

if __name__ == "__main__":
  answer = count_tilde(P)
  print(answer)