import os
from os import listdir
from os.path import isfile, join


def get_directory_files(path):
    result = []
    [result.append(file) for file in listdir(path) if isfile(join(path, file))]
    return result


pattern = "{:<8} {:<15} {:<10} {:<10} {:<20}"


def list_directory_files(path):
    files = get_directory_files(path)
    print(pattern.format('Mode', 'Owner', 'Group', 'Size', 'File name'))
    [print(pattern.format(os.stat(file).st_mode, os.stat(file).st_uid,
                          os.stat(file).st_gid, os.stat(file).st_size,
                          os.path.basename(file))) for file in files]
