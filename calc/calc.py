# -*- coding: utf-8 -*-
from functools import reduce

class Calc:
    def add(self, *args) -> int:
        return sum(args)

    def sub(self, a, b) -> int:
        return a - b

    def mul(self, *args) -> int:
        # def mul2(a, b):
        #     return a * b
        #return reduce(mul2, args)
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b) -> float:
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"