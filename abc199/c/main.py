N = int(input())
S = list(input())
Q = int(input())

query = []
for i in range(Q):
  T, A, B = map(int, input().split())
  query.append([T, A, B])

isNormal = True
for i in range(Q):
  T = query[i][0]
  if T == 1:
    if isNormal == True:
      Ai = query[i][1] - 1 #int
      Bi = query[i][2] - 1 #int
      tmp = S[Ai]
      S[Ai] = S[Bi]
      S[Bi] = tmp
    else:
      Ai = query[i][1] - 1 #int
      Bi = query[i][2] - 1 #int
      if Ai < N:
        Ai += N
      else:
        Ai -= N
      if Bi < N:
        Bi += N
      else:
        Bi -= N
      tmp = S[Ai]
      S[Ai] = S[Bi]
      S[Bi] = tmp
  elif T == 2:
    isNormal = not isNormal

if not isNormal:
  str_front = S[:N]
  str_end = S[N:2*N]
  print("".join(str_end + str_front))
else:
  print("".join(S))