from dataclasses import dataclass
from typing import NamedTuple


class Range(NamedTuple):
    min: int
    max: int

    @staticmethod
    def neighborhood(base: int, range: int):
        return Range(base - range, base + range)

    def extended(self, range: int):
        return Range(self.min - range, self.max + range)

    def intersection(self, other):
        return Range(max(self.min, other.min), min(self.max, other.max))

    def iterate(self) -> range:
        return range(self.min, self.max+1)


class ManhattanRegion(NamedTuple):
    sum: Range
    diff: Range

    @staticmethod
    def neighborhood(x: int, y: int, distance: int):
        return ManhattanRegion(sum=Range.neighborhood(x+y, distance),
                               diff=Range.neighborhood(x-y, distance))

    def extended(self, delta: int):
        return ManhattanRegion(self.sum.extended(delta),
                               self.diff.extended(delta))

    def intersection(self, other):
        return ManhattanRegion(self.sum.intersection(other.sum),
                               self.diff.intersection(other.diff))

    def points(self):
        for sum in self.sum.iterate():
            for diff in self.diff.iterate():
                x, residue = divmod(sum + diff, 2)
                if residue == 0:
                    yield x, sum - x


def possible_locations(interval: int, accuracy: int, 
                       readings) -> list[tuple[int, int]]:
    location = ManhattanRegion.neighborhood(0, 0, 0)
    for x, y in readings:
        location = location.extended(interval)
        gps = ManhattanRegion.neighborhood(x, y, accuracy)
        location = location.intersection(gps)
    return list(location.points())


T, D, N = map(int, input().split())
GPS = (map(int, input().split()) for _ in range(N))
solutions = possible_locations(T, D, GPS)
print(len(solutions))
for solution in solutions:
    print(*solution)
