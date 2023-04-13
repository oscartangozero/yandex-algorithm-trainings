N, M = map(int, input().split())
A, B = map(set, ((int(input()) for _ in range(N)),
                 (int(input()) for _ in range(M))))
common = A.intersection(B)
for items in (common, A-common, B-common):
    print(len(items))
    print(*sorted(items))
