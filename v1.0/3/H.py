N = int(input())
birds = (map(int, input().split()) for _ in range(N))
bird_stacks = len(set(x for x, y in birds))
print(bird_stacks)