from collections import defaultdict


def count_previous(words: list[str]):
    count = defaultdict(int)
    for word in words:
        yield count[word]
        count[word] += 1

text = open('input.txt', 'r').read()
print(*count_previous(text.split()))


