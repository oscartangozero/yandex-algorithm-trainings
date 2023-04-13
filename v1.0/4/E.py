from collections import defaultdict


def highest_tower(blocks) -> int:
    highest_block = defaultdict(int)
    for width, height in blocks:
        highest_block[width] = max(highest_block[width], height)
    return sum(highest_block.values())


N = int(input())
WH = (map(int, input().split()) for _ in range(N))
print(highest_tower(WH))
