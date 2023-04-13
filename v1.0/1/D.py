def solve(a: int, b: int, c: int) -> str:
    if c == 0:
        return 'NO SOLUTION'
    if a == 0:
        return 'MANY SOLUTIONS' if b == c**2 else 'NO SOLUTION'
    x, residue = divmod(c**2 - b, a)
    return str(x) if residue == 0 else 'NO SOLUTION'


a, b, c = map(int, input().split())
print(solve(a, b, c))
