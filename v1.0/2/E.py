from bisect import bisect


def place(player: int, throws: list[int]) -> int:
    return len(throws) - bisect(sorted(throws), throws[player]) + 1


def best_place_for_vasily(throws: list[int]) -> int:
    throw_distance = throws.__getitem__
    left_bound = max(range(len(throws)), key=throw_distance) + 1
    possible_throwers = (i for i in range(left_bound, len(throws)-1)
                         if throws[i] % 10 == 5 and throws[i] > throws[i+1])
    best_thrower = max(possible_throwers, key=throw_distance, default=None)
    return place(best_thrower, throws) if best_thrower is not None else 0


n = int(input())
throws = list(map(int, input().split()))
print(best_place_for_vasily(throws))
