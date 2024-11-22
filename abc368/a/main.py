N, K = map(int, input().split())
A = list(input().split())

back = A[-K:]
tmp = A[:-(N-K)]
print(tmp)