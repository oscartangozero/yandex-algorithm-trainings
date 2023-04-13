def closest(numbers, target: int) -> int:
    return min(numbers, key=lambda v: abs(target-v))


N = int(input())
numbers = map(int, input().split())
x = int(input())
print(closest(numbers, x))
