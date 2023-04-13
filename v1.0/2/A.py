def are_monotonically_increasing(numbers: list[int]) -> bool:
    return all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1))


numbers = list(map(int, input().split()))
print('YES' if are_monotonically_increasing(numbers) else 'NO')
