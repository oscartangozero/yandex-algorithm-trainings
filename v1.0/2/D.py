def count_greater_than_neighbors(numbers: list[int]) -> int:
    return sum(numbers[i-1] < numbers[i] > numbers[i+1]
               for i in range(1, len(numbers)-1))


numbers = list(map(int, input().split()))
print(count_greater_than_neighbors(numbers))
