from collections import defaultdict
import math


def query_result(operations: list[str]):
    register = defaultdict(int)
    for record in operations:
        match record.split():
            case ['DEPOSIT', client, amount]:
                register[client] += int(amount)
            case ['WITHDRAW', client, amount]:
                register[client] -= int(amount)
            case ['BALANCE', client]:
                yield str(register[client]) if client in register else 'ERROR'
            case ['TRANSFER', sender, recipient, amount]:
                register[sender] -= int(amount)
                register[recipient] += int(amount)
            case ['INCOME', percentages]:
                rate = int(percentages) / 100
                for client, amount in register.items():
                    if amount > 0:
                        register[client] += math.floor(register[client] * rate)


operations = open('input.txt', 'r').read().splitlines()
print('\n'.join(query_result(operations)))
