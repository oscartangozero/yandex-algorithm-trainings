from collections import Counter, defaultdict


def mayan_occurences(word: str, text: str) -> int:
    window_size = len(word)
    word_counts = Counter(word)
    window_counts = Counter(text[:window_size])
    balance = defaultdict(int, {char: window_counts[char] - word_counts[char]
               for char in window_counts.keys() | word_counts.keys()})
    difference = sum(map(bool, balance.values()))
    occurences = (difference == 0)
    for i in range(window_size, len(text)):
        # print(f'{i=} {difference=} {balance=}')
        coming, going = text[i], text[i-window_size]
        for char, balance_change in ((coming, +1), (going, -1)):
            difference += (balance[char] == 0)
            balance[char] += balance_change
            difference -= (balance[char] == 0)
        occurences += (difference == 0)
    return occurences


G, _ = map(int, input().split())
W = input()
S = input()
print(mayan_occurences(W, S))
