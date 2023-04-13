def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and b + c > a and c + a > b


a, b, c = (int(input()) for _ in range(3))
print('YES' if is_valid_triangle(a, b, c) else 'NO')
