numbers = [*map(int, input().split())]
a, b, c = sorted(numbers[:3])
d, e = sorted(numbers[-2:])
print('YES' if a <= d and b <= e else 'NO')
