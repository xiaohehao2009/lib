def main():
    from fractions import Fraction as f
    from sys import set_int_max_str_digits as _f
    _f(0)
    n = f(input('输入一个数:'))
    a = [n]
    b = [0]
    # 0: call
    # 1: div2
    # 2: sub
    while len(b):
        c = b.pop()
        if c == 1:
            a[-1] /= 2
        elif c == 2:
            d = a.pop()
            a[-1] -= d
        else:
            if a[-1] < 0:
                a[-1] = -a[-1]
            else:
                a.append(a[-1] - 1)
                b += [1, 0, 2, 0]
    if len(a) != 1:
        print('a is', a)
        return
    print(f'f({n})=' + str(a[0]))


main()
