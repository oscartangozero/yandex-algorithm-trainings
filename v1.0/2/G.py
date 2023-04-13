from math import prod


def swap(data: list, i: int, j: int):
    data[i], data[j] = data[j], data[i]


def sort_ends(data: list[int], prefix: int, suffix: int):
    for i in range(0, prefix):
        swap(data, i, min(range(i, len(data)), key=data.__getitem__))
    for j in range(0, -suffix, -1):
        swap(data, j-1, max(range(len(data)+j), key=data.__getitem__))


def greatest_product_components(numbers: list[int]) -> tuple[int, int]:
    sort_ends(numbers, prefix=2, suffix=2)
    return tuple(max(numbers[:2], numbers[-2:], key=prod))


numbers = list(map(int, input().split()))
print(*greatest_product_components(numbers))
