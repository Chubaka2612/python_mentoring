import os
from os import listdir
from os.path import isfile, join


def get_directory_files(path):
    result = []
    [result.append(file) for file in listdir(path) if isfile(join(path, file))]
    return result


def list_directory_files(path):
    files = get_directory_files(path)
    # as a variable
    print("{:<8} | {:<5} | {:<5} | {:<10} | {:<20}".format('Mode', 'Owner', 'Group', 'Size', 'File name'))
    for file in files:
        print("{:<8} | {:<5} | {:<5} | {:<10} | {:<20}".format(os.stat(file).st_mode, os.stat(file).st_uid,
                                                         os.stat(file).st_gid, os.stat(file).st_size,
                                                         os.path.basename(file)))
