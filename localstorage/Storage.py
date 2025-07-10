from . import j 
from pathlib import Path
import os


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
    

    def exists(self, file_name):
        return Path(self._path(file_name)).exists()


    def save(self, file_name, data):
        _assert_valid_value(data)

        j.save(self._path(file_name), data)


    def clear_list(self, file_name):
        self.save(file_name, [])



    def extend(self, file_name, obj):
        _assert_valid_value(obj)

        cached_array = self.get(file_name, [])

        if isinstance(obj, list):
            cached_array.extend(obj)
        else:
            cached_array.append(obj)

        self.save(file_name, cached_array)


    def append(self, file_name, obj): # rename to append_to_list?
        _assert_valid_value(obj)

        cached_array = self.get(file_name, [])
        cached_array.append(obj)
        self.save(file_name, cached_array)


    def append_key_to_dict(self, file_name, key, value):
        _assert_valid_value(key)
        _assert_valid_value(value)

        cached_dict = self.get(file_name, {})
        cached_dict[key] = value

        self.save(file_name, cached_dict)


    def folders_in(self, path):
        folders = []
        
        for item in Path(self._path(path)).iterdir():
            if item.is_dir():
                folders.append(item.name)
        
        return folders


    def all_files(self, filename=None):
        files = []

        x = self.base_path + "localstorage/"
        for i in Path(x).rglob("*"):
            if i.is_file():
                if filename is None or i.name == filename:
                    files.append(i)

        return files

