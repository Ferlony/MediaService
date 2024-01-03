import json


def read_decorator(fun):
    def inner_fun(path: str):
        try:
            return fun(path)
        except Exception as e:
            print(e)
            return None
    return inner_fun


@read_decorator
def read_file_path(path: str):
    with open(path, 'r') as f:
        return f.read()


@read_decorator
def read_json(path: str):
    with open(path, 'r') as f:
        return json.load(f)
