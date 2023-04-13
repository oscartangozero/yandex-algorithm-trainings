from functools import partial


def address(room, building_height, floor_size) -> tuple[int, int] | None:
    block, block_index = divmod(room, building_height * floor_size)
    floor, floor_index = divmod(block_index, floor_size)
    return (block, floor) if floor_index < floor_size else None


def guess_floor_size(room, block, floor, building_height) -> range:
    floors_before = building_height * block + floor
    return range(room // (floors_before + 1) + 1, room // floors_before + 1)


def solve(k1, m, k2, p2, n2) -> tuple[int, int]:
    if n2 > m:
        return -1, -1
    if p2 == n2 == 1:
        if k1 < k2:
            return 1, 1
        floor_size = range(k2, k1+1)
    else:
        floor_size = guess_floor_size(k2-1, p2-1, n2-1, m)
    solutions = [*filter(None, map(partial(address, k1-1, m), floor_size))]
    if len(solutions) == 0:
        return -1, -1
    p1, n1 = map(set, zip(*solutions))
    return (p1.pop() + 1 if len(p1) == 1 else 0,
            n1.pop() + 1 if len(n1) == 1 else 0)


k1, m, k2, p2, n2 = map(int, input().split())
print(*solve(k1, m, k2, p2, n2))
