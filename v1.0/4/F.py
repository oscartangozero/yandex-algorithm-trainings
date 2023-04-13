from collections import defaultdict


def print_sales_report(records: list[str]):
    register = defaultdict(lambda: defaultdict(int))
    for record in records:
        customer, item, amount = record.split()
        register[customer][item] += int(amount)

    for customer in sorted(register.keys()):
        print(customer + ':')
        for item, amount in sorted(register[customer].items()):
            print(item, amount)


records = open('input.txt', 'r').read().splitlines()
print_sales_report(records)
