from collections import deque

N, Q = map(int, input().split())

A = []
for i in range(N):
    A.append(i + 1)

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A[query[1] - 1] = query[2]
    elif query[0] == 2:
        print(A[query[1] - 1])
    elif query[0] == 3:
        # (N-1)までならOK
        # N = q[1]は何もしない
        # N % q[1]のあまりがが変更する回数？
        q = query[1]
        if not N == q:
            times = q % N
            d = deque(A)
            d.rotate(-times)
            A = list(d)
