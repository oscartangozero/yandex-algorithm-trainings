first, second = (map(int, input().split()) for _ in range(2))
print(*sorted(set(first).intersection(second)))
