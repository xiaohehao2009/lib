class Node:
    def __init__(self, value, parent, children):
        self.value = value
        self.parent = parent
        self.children = children
    def add_last_child(self, child):
        if child == self:
            raise ValueError('Cannot add a tree to its children')
        self.children.append(child)
    def remove_last_child(self):
        if self.has_no_child():
            raise ValueError('The tree has no children to remove')
        self.children.pop()
    def has_no_child(self):
        return not self.children
    def has_child(self):
        return bool(self.children)
    def copy_and_join(self, newparent):
        node = Node(self.value, newparent, [])
        for child in self.children:
            child.copy_and_join(node)
        newparent.add_last_child(node)
        return node


def iter_calc_hydra(num, hydra):
    if hydra.value != 1 or hydra.parent is not None:
        raise ValueError('Not invalid hydra sequence')
    yield hydra
    if hydra.has_no_child():
        return
    rb = hydra # right bottom
    while rb.has_child():
        rb = rb.children[-1]
    while True:
        if rb.has_child():
            print('aborted hydra:', hydra_tostr(hydra))
            print('aborted rb:', hydra_tostr(rb))
            return
        if rb.value == 1:
            rbpar = rb.parent
            rbppar = rbpar.parent
            if rbppar is None:
                return
            rbpar.remove_last_child()
            for i in range(1, num):
                rbpar.copy_and_join(rbppar)
            rb = rbppar.children[-1]
            while rb.has_child():
                rb = rb.children[-1]
            yield hydra
            continue
        # print('=' * 8, 'start drop')
        rbpar = rb.parent
        father_item = rbpar
        # print('rb:', hydra_tostr(rb))
        # print('rbpar:', hydra_tostr(rbpar))
        while father_item.value >= rb.value:
            father_item = father_item.parent
        # print('father_item:', hydra_tostr(father_item))
        rbpar.remove_last_child()
        flag = rbpar.has_no_child()
        # print('now rbpar:', hydra_tostr(rbpar))
        # print('now father_item:', hydra_tostr(father_item))
        # print('now hydra:', hydra_tostr(hydra))
        for i in range(1, num):
            # print('=' * 8, 'start copy')
            father_item = father_item.copy_and_join(rbpar)
            # print('copied:', hydra_tostr(copied))
            # print('now rbpar:', hydra_tostr(rbpar))
            # print('now father_item:', hydra_tostr(father_item))
            # print('now hydra:', hydra_tostr(hydra))
            rb = father_item
            while rb.has_child():
                rb = rb.children[-1]
            rbpar = rb if flag else rb.parent
            # print('rb:', hydra_tostr(rb))
            # print('rbpar:', hydra_tostr(rbpar))
        yield hydra
    return


def hydra_tostr(hydra):
    callee_str = f'p{hydra.value}'
    if hydra.has_no_child():
        return callee_str
    arg_str_list = [hydra_tostr(child) for child in hydra.children]
    args_str = '+'.join(arg_str_list)
    return f'{callee_str}({args_str})'


def main():
    root = Node(1, None, [])
    second_layer = Node(2, root, [])
    third_layer = Node(2, second_layer, [])
    # third_layer2 = Node(1, second_layer, [])
    root.add_last_child(second_layer)
    second_layer.add_last_child(third_layer)
    # second_layer.add_last_child(third_layer2)
    print('\\displaystyle')
    print('\\begin{align}')
    for hydra in iter_calc_hydra(3, root):
        print('& \\bigm/', hydra_tostr(hydra), '\\\\')
    print('\\end{align}')


if __name__ == '__main__':
    main()
