from copy import deepcopy
from numbers import Number


def isnum(obj) -> bool:
    return isinstance(obj, Number)


def check2dnumlist(obj, name: str) -> None:
    if not isinstance(obj, list):
        raise Exception(f'{name} is not a list')
    for i, p in enumerate(obj):
        if not isinstance(p, list):
            raise Exception(f'{name}[{i}] is not a list')
        for j, num in enumerate(p):
            if not isnum(num):
                raise Exception(f'{name}[{i}][{j}] is not a number')


def checknumlist(obj, name: str) -> None:
    if not isinstance(obj, list):
        raise Exception(f'{name} is not a list')
    for i, p in enumerate(obj):
        if not isnum(p):
            raise Exception(f'{name}[{i}] is not a number')


def nonelist(size: int) -> list:
    return [None for i in range(size)]


def lewmu(matrix0: list[list]) -> list:
    '''
        Linear Equations With Many Unknowns:
        input a matrix of a group of
            linear equations with many unknowns
            like this: [
            [1, 0, 1],
            [0, 1, 0]
        ]
        output a group of numbers
            like this: [1, 0]
        if:
            the matrix is not a list[list[int]]
                like this: [['1', 1]]
            the matrix is not in format
                like this: [[1, 1], [2, 2]]
                format: (width = height + 1)
        then: raise
    '''
    # check & copy
    check2dnumlist(matrix0, 'matrix0')
    size = len(matrix0) + 1
    for i, line in enumerate(matrix0):
        if len(line) != size:
            raise Exception(f'matrix0[{i}]\'s size not correct')
    matrix = deepcopy(matrix0)

    # start calc
    for i in range(size - 2):
        # check & move
        if not matrix[i][i]:
            flag = False
            for j in range(i + 1, size - 1):
                if matrix[j][i]:
                    replace_index = j
                    flag = True
                    break
            if flag:
                matrix[i], matrix[j] = matrix[j], matrix[i]
            else:
                raise Exception('unable to calculate')
        # calc in line
        line0 = matrix[i]
        base = line0[i]
        for j in range(i + 1, size - 1):
            line = matrix[j]
            rate = line[i] / base
            line[i] = 0
            for k in range(i + 1, size):
                line[k] -= line0[k] * rate

    # matrix to results
    results = nonelist(size - 1)
    for i in range(size - 2, -1, -1):
        line = matrix[i]
        for j in range(size - 2, i, -1):
            line[-1] -= results[j] * line[j]
        results[i] = line[-1] / line[i]

    return results


def points_to_matrix(points: list[list]) -> list[list]:
    # check
    check2dnumlist(points, 'points')
    for i, p in enumerate(points):
        if len(p) != 2:
            raise Exception(f'points[{i}]\'s size not correct')

    # calc
    size = len(points)
    matrix = nonelist(size)
    for i, (x, y) in enumerate(points):
        line = nonelist(size + 1)
        for j in range(1, size):
            line[j] = x ** j
        line[0] = 1
        line[-1] = y
        matrix[i] = line

    return matrix


def func_to_expr(results: list) -> str:
    # check
    checknumlist(results, 'results')

    # calc
    size = len(results)
    items = nonelist(size)
    for i in range(size - 1, 0, -1):
        num = results[i]
        if not num:
            del items[i]
        elif num == 1:
            items[i] = f'+x**{i}' if i != 1 else '+x'
        elif num == -1:
            items[i] = f'-x**{i}' if i != 1 else '-x'
        else:
            items[i] = f'{num:+}*x**{i}' if i != 1 else f'{num:+}*x'
    if results[0]:
        items[0] = f'{results[0]:+}'
    else:
        del items[0]
    items.reverse()
    return f'f(x)={"".join(items)[1:]}'


def points_to_func(points: list[list]) -> list:
    return lewmu(points_to_matrix(points))


def points_to_expr(points: list[list]) -> str:
    return func_to_expr(points_to_func(points))


def calc_func(num, func: list) -> Number:
    # check
    if not isnum(num):
        raise Exception('num is not a number')
    checknumlist(func, 'func')

    # calc
    result = func[-1]
    size = len(func)
    for i in range(size - 2, -1, -1):
        result *= num
        result += func[i]

    return result


def data_to_points(data: list) -> list:
    if not isinstance(data, list):
        raise Exception('data is not a list')
    for i, num in enumerate(data):
        if not isnum(num):
            raise Exception(f'data[{i}] is not a number')
    return [[i, num] for i, num in enumerate(data)]


if __name__ == '__main__':
    points = [[i, abs(i)] for i in range(-10, 10)]
    num = 10
    print(points)
    func = points_to_func(points)
    print(func_to_expr(func))
    print(num, calc_func(num, func), sep=': ')
