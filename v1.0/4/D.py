from collections import Counter


def would_break(lifetime: list[int], clicks) -> list[bool]:
    wear = Counter(clicks)
    keys = range(1, len(lifetime) + 1)
    return [wear[key] > lifetime[key-1] for key in keys]


N = int(input())
C = list(map(int, input().split()))
K = int(input())
P = map(int, input().split())
print(*('YES' if would else 'NO' for would in would_break(C, P)), sep='\n')
