def truthful_turtles(total: int, statements) -> int:
    return len(set(a for a, b in statements if 0 < a + 1 == total - b <= total))


N = int(input())
AB = (map(int, input().split()) for _ in range(N))
print(truthful_turtles(N, AB))
