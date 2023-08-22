import tomllib
import importlib as im
import os.path as pt
import sys
from sys import modules
# from uuid import uuid4
from builtin_components import TopLine as builtinTL, Apps as builtinApps

dirname = pt.abspath(pt.dirname(__file__))

def process_modfile(file, processed=None):
    # get a file and returns the module
    if not pt.isabs(file):
        file = pt.join(dirname, file)
    if not pt.lexists(file):
        raise Exception(f'No such file: {file}, is it a mistake in \
your config file?')
    try:
        file = pt.realpath(file, strict=True)
    except OSError:
        raise Exception(f'Invalid file: {file}, is it a mistake in \
your config file?')
    if processed is not None:
        if file in processed:
            raise Exception(f'Module {file} appeared in your config \
file repeatedly')
        processed.add(file)
    # modname = str(uuid4())
    # spec = ut.spec_from_location(modname, file)
    # mod = ut.module_from_spec(spec)
    # modules[modname] = mod
    file_dir, file_name = pt.split(file)
    if pt.isdir(file):
        if '.' in file_name:
            raise Exception(f'Invalid package name: {file_name}')
        sys.path.append(file_dir)
        package = im.import_module(file_name)
        sys.path.pop()
        if not hasattr(package, 'export'):
            raise Exception(f'Invalid module: {file}')
        return package.export
    if file_name.count('.') > 1:
        raise Exception(f'Invalid module name: {file_name}')
    sys.path.append(file_dir)
    mod = im.import_module(file_name.partition('.')[0])
    sys.path.pop()
    if not hasattr(mod, 'export'):
        raise Exception(f'Invalid module: {file}')
    return mod.export

def process_modules(files):
    processed = set()
    mods = []
    for file in files:
        if file == '<builtin>':
            if file in processed:
                raise Exception('Module <builtin> appeared in your \
config file repeatedly')
            mods += builtinApps
            processed.add(file)
            continue
        mods.append(process_modfile(file, processed))
    return tuple(mods)


def get_table():
    table = (
        # each attribute here correspond to the args given to main module
        ('topline', str, process_modfile, builtinTL),
        ('app_components', list, process_modules, builtinApps),
        ('topline_mouse_area', int, lambda x: x, 2)
    )
    return table


def process_table(data, table):
    arr = []

    def destruct(name, target_type=object, process_function=object,
        default_value=None, strict=True, *_):
        return str(name), target_type, process_function, \
            default_value, strict

    for row in table:
        # row's structure:
        # name, type, process_function, default_value, strict
        if len(row) == 0:
            raise Exception(f'(internal implement) Not an available table \
row: {row}')
        name, target_type, process_function, \
            default_value, strict = destruct(*row)
        if name not in data:
            if default_value is None:
                raise Exception(f'Name {name} not defined in your config \
file')
            arr.append(default_value)
            continue
        value = data[name]
        if not isinstance(value, target_type):
            if (not strict and default_value is None) or strict:
                raise Exception(f'Not an available value: {value}, expected \
type {target_type}, but received type {type(value)}')
            arr.append(default_value)
            continue
        arr.append(process_function(value))
    return tuple(arr)


def get_datas():
    config_file = 'config.toml'
    config_path = pt.join(dirname, config_file)

    # load config file
    if not pt.lexists(config_path):
        # load default components
        import builtin_components as btc
        return (btc.TopLine, btc.Apps)
    if not pt.isfile(config_path):
        raise Exception(f'Not a file: {config_path}')
    with open(config_path, 'rb') as file:
        data = tomllib.load(file)

    return process_table(data, get_table())

if __name__ == '__main__':
    print(get_datas())
