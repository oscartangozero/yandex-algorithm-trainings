from collections import Counter


def first_most_common(words: list[str]) -> str:
    return min(Counter(words).items(),
               key=lambda p: (-p[1], p[0]))[0]


text = open('input.txt', 'r').read()
print(first_most_common(text.split()))
