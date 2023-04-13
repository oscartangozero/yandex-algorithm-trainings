def smallest_arrangement(x1, y1, x2, y2) -> tuple[int, int]:
    arrangements = ((x1+x2, max(y1, y2)), (x1+y2, max(y1, x2)),
                    (y1+x2, max(x1, y2)), (y1+y2, max(x1, x2)))
    return min(arrangements, key=lambda s: s[0] * s[1])


x1, y1, x2, y2 = map(int, input().split())
print(*smallest_arrangement(x1, y1, x2, y2))
