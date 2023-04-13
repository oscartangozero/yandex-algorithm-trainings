def parts_output(material: int, block: int, part: int) -> int:
    if not (material >= block >= part):
        return 0
    parts_per_block, leftover_per_block = divmod(block, part)
    parts_produced = 0
    while material >= block:
        blocks_number, material = divmod(material, block)
        parts_produced += parts_per_block * blocks_number
        material += leftover_per_block * blocks_number
    return parts_produced

N, M, K = map(int, input().split())
print(parts_output(N, M, K))
