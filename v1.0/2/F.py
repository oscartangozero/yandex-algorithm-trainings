def prefix_func(s: list) -> list:
    p = [0] * len(s)
    for i in range(1, len(s)):
        j = p[i-1]
        while j > 0 and s[i] != s[j]:
            j = p[j-1]
        p[i] = j + (s[i] == s[j])
    return p


def palindrome_suffix_start(items: list[int]) -> int:
    suffix_matches = prefix_func([*reversed(items), None, *items])[-len(items):]
    for end, length in enumerate(suffix_matches, start=1):
        if end + 1 + length >= len(items):
            return end - length


N = int(input())
numbers = list(map(int, input().split()))
pad_size = palindrome_suffix_start(numbers)
print(pad_size)
print(*reversed(numbers[:pad_size]))
