def main():
    from fractions import Fraction as f
    from sys import set_int_max_str_digits
    set_int_max_str_digits(0)
    u = input()
    if u[0] == 'u':
        n = f(u[1:])
    else:
        n = f(u)
    a = [n]
    b = [0]
    map = {}
    # 0: call
    # 1: div2 and record
    # 2: sub
    while len(b):
        c = b.pop()
        if c == 1:
            a[-1] /= 2
            if a[-2].denominator <= 33554432:
                map[a[-2]] = a[-1]
            del a[-2]
        elif c == 2:
            d = a.pop()
            a[-1] -= d
        else:
            d = a.pop()
            if d < 0:
                a.append(-d)
            else:
                if d in map:
                    a.append(map[d])
                    continue
                a += [d, d, d - 1]
                b += [1, 0, 2, 0]
    if u[0] == 'u':
        print(a[0])
        return
    for i in list(map.keys()):
        if i.denominator <= 1024:
            print(f'{i}: ', end='')
            print(map[i])


main()
