import fnmatch
import os

def find(path, name, f_type):
    result = []
    for root, dirs, files in os.walk(path):
        if f_type == "f":
            [result.append(os.path.join(root, f_name)) for f_name in files if fnmatch.fnmatch(f_name, name)]
        elif f_type == "d":
            [result.append(os.path.join(root, d_name)) for d_name in dirs if fnmatch.fnmatch(d_name, name)]
        else:
            raise Exception("Invalid parameter is entered")
    return result
