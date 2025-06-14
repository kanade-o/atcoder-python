N, Q = map(int, input().split())
X = list(map(int, input().split()))

ans = [0] * Q
boxes = [0] * N
for i in range(Q):
    if X[i] >= 1:
        boxes[X[i] - 1] += 1
        ans[i] = X[i]
    else:
        min_index = min([(boxes[i], i) for i in range(N)])[1]
        boxes[min_index] += 1
        ans[i] = min_index + 1
print(*ans)
