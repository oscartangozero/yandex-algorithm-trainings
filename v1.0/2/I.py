def render_field(height: int, width: int, mines: list[tuple[int, int]]) -> str:
    field = [[0] * (width+1) for _ in range(height+1)]
    for y, x in mines:
        for i in range(y-2, y+1):
            for j in range(x-2, x+1):
                field[i][j] += 1
    for y, x in mines:
        field[y-1][x-1] = '*'  # type: ignore
    return '\n'.join(
        ' '.join(str(field[y][x]) for x in range(width))
        for y in range(height))


N, M, K = map(int, input().split())
pqs = [tuple(map(int, input().split())) for _ in range(K)]
print(render_field(N, M, pqs))
