X, K, D = map(int, input().split())

X = abs(X)

if 0 < X-K*D:
  print(abs(X-K*D))
else:
  times_before_pass = K - X//D
  coordinate_before_pass = X - (X//D)*D
  coordinate_after_pass = coordinate_before_pass - D
  if times_before_pass % 2 == 0:
    print(abs(coordinate_before_pass))
  else:
    print(abs(coordinate_after_pass))