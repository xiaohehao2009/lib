# f(x)=\begin{cases}-x&x<0\\0.5f(x-f(x-1))&x\gte0\end{cases}

def main(usefast = False):
    from fractions import Fraction as frac
    from sys import set_int_max_str_digits
    set_int_max_str_digits(0)
    str_input = input('计算f(x): ')
    if str_input.lower() in ('quit', 'exit', 'q', 'x', 'n', 'no', '', ':q', ';', ':', ':wq', ':qw', ':x', 'nan', 'n/a'):
        print('Aborted')
        return
    user_input = frac(str_input)
    eval_stack = [user_input]
    code_stack = [0]
    # 0: call
    # 1: div2
    # 2: sub & call
    const_array = [1, 2, 0]
    const_array_2 = [1, 0]
    const_array_3 = [1, 2]
    const_color = ['48;5;51m', '48;5;81m', '48;5;111m']
    const_delay = 0.005
    code_stack_pop = code_stack.pop
    code_stack_extend = code_stack.extend
    eval_stack_append = eval_stack.append
    eval_stack_pop = eval_stack.pop
    from time import sleep
    def output_frac(num, end=''):
        if num.denominator == 1:
            if num.numerator >= 0:
                return f'\x1b[33m{num.numerator}\x1b[m{end}'
            else:
                return f'-\x1b[33m{-num.numerator}\x1b[m{end}'
        elif num.numerator > 0:
            return f'\x1b[33m{num.numerator}\x1b[m/\x1b[33m{num.denominator}\x1b[m{end}'
        else:
            return f'-\x1b[33m{-num.numerator}\x1b[m/\x1b[33m{num.denominator}\x1b[m{end}'
    def join_fracs(fracs, sep=', ', end=''):
        return sep.join(output_frac(i) for i in fracs) + end
    def join_colors(colors, sep='', end=''):
        return sep.join(f'\x1b[{i} ' for i in colors) + '\x1b[m\x1b[K' + end
    fr12 = frac(1, 2)
    fr34 = frac(3, 4)
    fr78 = frac(7, 8)
    frf0 = frac(15, 16)
    while code_stack:
        if not usefast:
            sleep(const_delay)
            colors_str = join_colors((const_color[i] for i in code_stack))
            fracs_str = join_fracs(eval_stack)
            print(colors_str, fracs_str, flush=True)
        else:
            print(' ' * len(code_stack), ', '.join(str(i) for i in eval_stack))
        code = code_stack_pop()
        if code == 0:
            stack_top = eval_stack[-1]
            if stack_top < 0:
                eval_stack[-1] = -eval_stack[-1]
            elif stack_top < 1:
                if stack_top >= frf0:
                    eval_stack[-1] = stack_top * 2 - 1
                    code_stack_extend(const_array_2)
                elif stack_top < fr12:
                    eval_stack[-1] = fr12 - stack_top
                elif stack_top < fr34:
                    eval_stack[-1] = fr34 - stack_top
                elif stack_top < fr78:
                    eval_stack[-1] = fr78 - stack_top
                elif stack_top < frf0:
                    eval_stack[-1] = frf0 - stack_top
            else:
                code_stack_extend(const_array)
                eval_stack_append(eval_stack[-1] - 1)
        elif code == 1:
            eval_stack[-1] /= 2
        else:
            cache = eval_stack[-1] = eval_stack[-2] - eval_stack_pop()
            if cache < 0:
                eval_stack[-1] = -cache
            elif cache < 1:
                code_stack_extend(const_array_3)
                eval_stack_append(1 - cache)
            else:
                code_stack_extend(const_array)
                eval_stack_append(cache - 1)
    print(output_frac(user_input, end=': ') + output_frac(eval_stack[0]))


from sys import argv
if len(argv) > 2:
    raise RangeError('argv too long')
if len(argv) > 1:
    if argv[1].lower() not in ('fast', 'f', 'quick', 'q', '-f', '-q'):
        raise RangeError('invalid argv')
    usefast = True
else:
    usefast = False

main(usefast)
