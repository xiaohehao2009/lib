def main(num):
    from sys import set_int_max_str_digits
    from fractions import Fraction as fr
    set_int_max_str_digits(0)

    print('注意到 f(x)=1/2-x, 0<=x<0.5, f(2x-1)/2, 0.5<=x<1\n')
    ev = [fr(num)]
    mp = {}
    fr12 = fr('1/2')
    while ev:
        a = ev.pop()
        if a in mp:
            unexist_var
        if a < 0:
            print(f'{a}: {-a}')
        elif 0 <= a < fr12:
            b = fr12 - a
            print(f'{a}: {b}')
            mp[a] = b
        elif fr12 <= a < 1:
            b = a * 2 - 1
            if b in mp:
                c = mp[b] / 2
                print(f'{a}: {c}')
                mp[a] = c
            else:
                print(a)
                ev.append(a)
                ev.append(b)
        else:
            b = a - 1
            if b in mp:
                c = a - mp[b]
                if c in mp:
                    d = mp[c] / 2
                    print(f'{a}: {d}')
                    mp[a] = d
                else:
                    ev.append(a)
                    ev.append(c)
            else:
                print(a)
                ev.append(a)
                ev.append(b)
    print('\nQuestion Easily Done!')


main(input('已知燃烧数函数f(x),求f(.):'))
