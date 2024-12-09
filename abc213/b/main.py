N = int(input())
A = list(map(int, input().split()))

sorted = sorted(A)
target = sorted[N-2]

print(A.index(target)+1)