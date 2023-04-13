from collections import defaultdict


def stress_number(word: str) -> int:
    return sum(map(str.isupper, word))


def is_stress_correct(word: str, variants: set[str]) -> bool:
    return word in variants if len(variants) > 0 else stress_number(word) == 1


def stress_errors(words: list[str], dictionary: dict[str, set[str]]) -> int:
    return sum(not is_stress_correct(word, dictionary[word.lower()])
               for word in words)


N = int(input())
dictionary = defaultdict(set)
for _ in range(N):
    word = input()
    dictionary[word.lower()].add(word)
task = input().split()
print(stress_errors(task, dictionary))
