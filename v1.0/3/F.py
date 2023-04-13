def sliding_window(sequence, n: int):
    return (sequence[i:i+2] for i in range(len(sequence) - 1))


def kinship_degree(first: str, second: str) -> int:
    second_pairs = set(sliding_window(second, 2))
    return sum(first_pair in second_pairs 
               for first_pair in sliding_window(first, 2))


first, second = (input() for _ in range(2))
print(kinship_degree(first, second))
