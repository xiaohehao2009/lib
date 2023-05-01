import operator
from fractions import Fraction
from numbers import Number
from copy import deepcopy
from time import time
from itertools import product, permutations

default_symbols = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


extra_symbols = default_symbols | {
    '%': operator.mod,
    '**': operator.pow
}


isnum = lambda obj: isinstance(obj, Number)


def all_matrixes(nums: tuple) -> list[list]:
    size = len(nums)
    if size <= 2:
        return [nums]
    if size == 3:
        return [(nums[:2], nums[2]), (nums[0], nums[1:])]
    results = []
    for i in range(1, size):
        arr = nums[0:i]
        if i == 1:
            prearrs = arr
        else:
            prearrs = all_matrixes(arr)
        if i == size - 1:
            postarrs = nums[i:]
        else:
            postarrs = all_matrixes(nums[i:])
        for postarr in postarrs:
            for prearr in prearrs:
                results.append((prearr, postarr))
    return results


def dosym(sym, pre, post):
    try:
        return sym[1](pre, post)
    except:
        return None


def calc(order: tuple, matrix: tuple,
    syms: tuple[tuple], curs: int = 0) -> tuple[Number]:
    # input order: [1,2,3,4,5]
    #       matrix: [[[0,1],2],[3,4]]
    #       syms: [+ - * /]
    # output (((0+1)-2)*(3/4))=-3/4
    m0 = matrix[0]
    m1 = matrix[1]
    if isinstance(m0, tuple):
        n0, curs = calc(order, m0, syms, curs)
    else:
        n0 = order[m0]
    sym = syms[curs]
    curs += 1
    if isinstance(m1, tuple):
        n1, curs = calc(order, m1, syms, curs)
    else:
        n1 = order[m1]
    return dosym(sym, n0, n1), curs


def calc_24card(nums: tuple, size: int, symbols: dict,
    target: Number) -> list[tuple]:
    if not isinstance(nums, tuple):
        raise Exception('nums is not a tuple')
    for i, num in enumerate(nums):
        if not isnum(num):
            raise Exception(f'nums[{i}] is not a number')

    matrixes = all_matrixes(tuple(range(size)))
    orders = tuple(set(permutations(nums, size)))
    syms = tuple(product(symbols.items(), repeat=size-1))
    results = []
    for order, matrix, sym in product(orders, matrixes, syms):
        result, _ = calc(order, matrix, sym)
        if result == target:
            results.append((order, matrix, sym))
    return results


def fraction_wrap(fraction: Fraction):
    return (str(fraction) if fraction.denominator == 1
        else f'({fraction})')


def item_to_str(order: tuple, matrix: tuple,
    syms: tuple[tuple], curs: int = 0) -> str:
    # input order: [8,3,8,3]
    #       matrix: [1, [2, [3, 4]]]
    #       syms: [/, -, /]
    # output 8 / (3 - (8 / 3))
    m0 = matrix[0]
    m1 = matrix[1]
    if isinstance(m0, tuple):
        n0, curs = item_to_str(order, m0, syms, curs)
    else:
        n0 = fraction_wrap(order[m0])
    sym = syms[curs][0]
    curs += 1
    if isinstance(m1, tuple):
        n1, curs = item_to_str(order, m1, syms, curs)
    else:
        n1 = fraction_wrap(order[m1])
    return f'({n0}{sym}{n1})', curs


def results_to_str(results: list[tuple[list]], target: Number = 24) -> str:
    arr = [f'{item_to_str(i[0], i[1], i[2])[0]}={target}' for i in results]
    return '  '.join(arr)


def symbols_to_str(symbols: dict):
    return ', '.join([i for i, _ in symbols.items()])


def str_or_num_to_nums(nums: tuple[str | Number]) -> tuple[Fraction]:
    return tuple(map(Fraction, nums))


def calc_and_print(nums: tuple[str | Number], size = None,
    syms: dict = default_symbols, target: Number = 24):
    nums = str_or_num_to_nums(nums)
    if size == None:
        size = len(nums)
    start = time()
    results = calc_24card(nums, size, syms, target)
    end = time()
    print(f'[{", ".join(map(str, nums))}] ---> {target}')
    print(f'with symbols {symbols_to_str(syms)}')
    print(f'{len(results)} methods in total')
    print(f'time: {(end - start) * 1000:.3f} ms')
    print(results_to_str(results, target))


if __name__ == '__main__':
    calc_and_print((2,3,4,5,6), target=330)
    # print(all_matrixes(list(range(5))))
