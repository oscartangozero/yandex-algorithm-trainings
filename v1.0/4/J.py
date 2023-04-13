from collections import Counter
import re
import sys


def identifiers(code: str, leading_digit_allowed: bool):
    regexp = r'\b\w*[A-Za-z_]\w*\b' if leading_digit_allowed \
        else r'\b[A-Za-z_]\w*\b'
    return (match.group() for match in re.finditer(regexp, code, re.ASCII))


def not_keyword(items, keywords: set[str], case_sensitive: bool):
    if not case_sensitive:
        keywords = set(map(str.lower, keywords))
        items = map(str.lower, items)
    return (item for item in items if item not in keywords)


def most_common(items) -> str:
    return Counter(items).most_common(1)[0][0]


N, *CD = input().split()
N, (C, D) = int(N), (word == 'yes' for word in CD)
keywords = set(input() for _ in range(N))
code = sys.stdin.read()
print(most_common(not_keyword(identifiers(code, D), keywords, C)))
