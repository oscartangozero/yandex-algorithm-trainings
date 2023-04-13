from operator import lt, eq, gt

SEQUENCE_TYPES = {(False, True, False): 'CONSTANT',
                  (True, False, False): 'ASCENDING',
                  (True, True, False): 'WEAKLY ASCENDING',
                  (False, False, True):  'DESCENDING',
                  (False, True, True): 'WEAKLY DESCENDING'}


def any_consecutive(items: list, predicate) -> bool:
    return any(predicate(items[i], items[i+1]) for i in range(len(items)-1))


def sequence_type(sequence: list[int]) -> str:
    ordering = tuple(any_consecutive(sequence, pred) for pred in (lt, eq, gt))
    return SEQUENCE_TYPES.get(ordering, 'RANDOM')  # type: ignore


STOP = -2 * 10**9
numbers = []
while (x := int(input())) != STOP:
    numbers.append(x)
print(sequence_type(numbers))
