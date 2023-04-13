TimeSpan = tuple[int, int]


def time_estimate(interval: int, count: int) -> TimeSpan:
    return (count + interval * (count - 1),
            count + interval * (count + 1))


def span_overlap(a: TimeSpan, b: TimeSpan) -> TimeSpan | None:
    overlap = max(a[0], b[0]), min(a[1], b[1])
    return overlap if overlap[0] <= overlap[1] else None


a, b, n, m = (int(input()) for _ in range(4))
print(*span_overlap(time_estimate(a, n), time_estimate(b, m)) or [-1])
