import json

def _assert_valid_value(o):
    if o == None:
        raise Exception("invalid value was passed into localstorage")

def get(file_name, default):
    _assert_valid_value(default)

    try:
        with open(f'localstorage/files/{file_name}.json', 'r') as f:
            return json.load(f)
    except:
        print("File not present, using default")
        return default


def save(file_name, o):
    _assert_valid_value(o)

    with open(f'localstorage/files/{file_name}.json', 'w') as f:
        json.dump(o, f, indent=4, sort_keys=True)


def get_single_value(name, value):
    return get(name, {'value': value})['value']

def save_single_value(name, value):
    save(name, {'value': value})

def append(file_name, o):
    _assert_valid_value(o)

    array = get(file_name, [])
    array.append(o)

    save(file_name, array)

    print(f"appending {o} to {file_name}")
