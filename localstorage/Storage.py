from . import j 


def _assert_valid_value(o):
    if o is None:
        raise Exception("invalid value was passed into localstorage")


class Storage:
    def __init__(self, base_path="./"):
        self.base_path = base_path

    def _path(self, file_name):
        return self.base_path + "localstorage/" + file_name


    def get(self, file_name, default):
        _assert_valid_value(default)

        return j.get(self._path(file_name), default)


    def save(self, file_name, data):
        _assert_valid_value(data)

        j.save(self._path(file_name), data)


    def append(self, file_name, o):
        _assert_valid_value(o)

        a = self.get(file_name, [])
        a.append(o)
        self.save(file_name, a)
