import os


def get_dirs_in_path(path):
    return os.listdir(path)


def walk_in_path(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
    return files


def get_all_files_in_directory(directory, path):
    if directory in get_dirs_in_path(path):
        return walk_in_path(path + directory)
    else:
        return None
