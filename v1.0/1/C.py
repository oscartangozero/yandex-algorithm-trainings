def phone_number(s: str) -> int:
    n = ''.join(filter(str.isdigit, s))
    if len(n) == 7:
        return int('495' + n)
    elif len(n) == 11:
        return int(n[1:])
    else:
        raise ValueError


new = phone_number(input())
old = [phone_number(input()) for _ in range(3)]
for number in old:
    print('YES' if new == number else 'NO')
