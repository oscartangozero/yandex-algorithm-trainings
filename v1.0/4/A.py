N = int(input())
synonyms = (input().split() for _ in range(N))
dictionary = {}
for first, second in synonyms:
    dictionary[first] = second
    dictionary[second] = first
word = input()
print(dictionary[word])
