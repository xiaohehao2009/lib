def main():
    import sys
    sys.set_int_max_str_digits(0)
    user_input = input('输入: ')
    parse_result = parse(user_input)
    calc_result = calcualte(*parse_result)
    print('输出:', calc_result)


def parse(user_input):
    eval_result = eval('(' + user_input + ')')
    if type(eval_result) != tuple:
        eval_result = (eval_result,)
    return (list(eval_result[:-1]), eval_result[-1])


def calculate(left, right):
    if right < 1 or not is_available(left) or not is_normal(left):
        return
    while left:
        last_item = left.pop()
        if last_item == 1:
            right += 1
        else:
            if last_item == 2 and left[-1] == 1:
                left.pop()
                right <<= 1
                continue
            if last_item == 2 and left[-1] == 2 and left[-2] == 1:
                del left[-2:]
                right <<= right
                continue
            for index in range(len(left) - 1, -1, -1):
                if left[index] + 1 == last_item:
                    bad_root = index
                    break
            left += left[bad_root:] * (right - 1)
    return right


def is_available(left):
    if not left:
        return False
    if left[0] != 1:
        return False
    for index in left:
        if index < 1:
            return False
    for index in range(1, len(left)):
        if left[index] > left[index - 1] + 1:
            return False
    return True


def is_normal(left, target_number=1):
    pool, last_pool = [], [left]
    for array in last_pool:
        if target_number not in array:
            continue
        index = last_index = array.index(target_number)
        for index in range(index + 1, len(array)):
            if array[index] == target_number:
                pool.append(array[last_index:index])
                last_index = index
        pool.append(array[last_index:])
    if not pool:
        return True
    for index in range(1, len(pool)):
        if dict_gt(pool[index], pool[index - 1]):
            return False
    for array in pool:
        if not is_normal(array, target_number + 1):
            return False
    return True
    # 1, 1, 2 => (1), (1, 2)
    # (1) < (1, 2)
    # 1, 2, 2, 3 => (2), (2, 3)
    # (2) < (2, 3)
    # 1, 2, 3, 4, 3, 4, 5 => ... => (3, 4), (3, 4, 5)
    # (3, 4) < (3, 4, 5)


def dict_gt(left, right):
    for index in range(min(len(left), len(right))):
        if left[index] > right[index]:
            return True
        if left[index] < right[index]:
            return False
    return len(left) > len(right)


if __name__ == '__main__':
    main()
