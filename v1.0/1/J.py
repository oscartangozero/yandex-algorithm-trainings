from enum import StrEnum


class Case(StrEnum):
    NONE = '0'
    LINE = '1 {k} {b}'
    POINT = '2 {x} {y}'
    EXACT_X = '3 {x}'
    EXACT_Y = '4 {y}'
    MANY = '5'


class Solution:
    def __init__(self, type: Case, **kwargs) -> None:
        self.type = type
        self.args = kwargs

    def __lt__(self, other) -> bool:
        return self.type < other.type

    def __str__(self) -> str:
        return self.type.format(**self.args)


def solve_equation(a: float, b: float, c: float) -> Solution:
    if a == 0 and b == 0:
        return Solution(Case.MANY if c == 0 else Case.NONE)
    if a == 0:
        return Solution(Case.EXACT_Y, y=c/b)
    if b == 0:
        return Solution(Case.EXACT_X, x=c/a)
    return Solution(Case.LINE, k=-a/b, b=c/b)


def solve_system(a: float, b: float, c: float,
                 d: float, e: float, f: float) -> Solution | None:
    first, second = sorted((solve_equation(a, b, e), solve_equation(c, d, f)))
    if first.type == Case.NONE or second.type == Case.MANY:
        return first
    if first.type == Case.LINE:
        k1, b1 = first.args.values()
        if second.type == Case.LINE:
            k2, b2 = second.args.values()
            if k1 == k2:
                return first if b1 == b2 else Solution(Case.NONE)
            x = (b2 - b1) / (k1 - k2)
            return Solution(Case.POINT, x=x, y=k1*x+b1)
        if second.type == Case.POINT:
            x, y = second.args.values()
            return second if y == k1 * x + b1 else Solution(Case.NONE)
        if second.type == Case.EXACT_X:
            x = second.args['x']
            return Solution(Case.POINT, x=x, y=k1*x+b1)
        if second.type == Case.EXACT_Y:
            y = second.args['y']
            return Solution(Case.POINT, x=(y-b1)/k1, y=y)
    if first.type == second.type:
        return first if first.args == second.args else Solution(Case.NONE)
    if first.type == Case.POINT:
        x, y = first.args.values()
        if (second.type == Case.EXACT_X and x == second.args['x']) or \
                (second.type == Case.EXACT_Y and y == second.args['y']):
            return first
        return Solution(Case.NONE)
    if first.type == Case.EXACT_X and second.type == Case.EXACT_Y:
        return Solution(Case.POINT, x=first.args['x'], y=second.args['y'])


a, b, c, d, e, f = (float(input()) for _ in range(6))
print(solve_system(a, b, c, d, e, f))
