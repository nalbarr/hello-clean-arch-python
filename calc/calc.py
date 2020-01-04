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
        
    def avg(self, xs, lt=None, ut=None) -> float:
        _xs = xs[:]

        if lt is not None:
            _xs = [x for x in _xs if x >= lt]

        if ut is not None:
            _xs = [x for x in _xs if x <= ut]

        if not len(_xs):
            return 0

        return sum(_xs) / len(_xs)