import os
from natsort import natsorted


def get_dirs_in_path(path):
    return os.listdir(path)


def sort_files(files):
    sorted_names = []
    sorted_paths = []
    sorted_dir_names = []
    out = []

    for each in files:
        sorted_names.append(each.get("name"))
        sorted_paths.append(each.get("path"))
        sorted_dir_names.append(each.get("dir_name"))

    sorted_names = natsorted(sorted_names)
    sorted_dir_names = natsorted(list(set(sorted_dir_names)))

    group_name = []
    group_path = []
    for i in range(0, len(sorted_names)):
        for j in range(0, len(sorted_names)):
            if sorted_names[i] in sorted_paths[j]:
                group_name.append(sorted_names[i])
                group_path.append(sorted_paths[j])

    for k in range(0, len(sorted_dir_names)):
        for i in range(0, len(group_path)):
            if sorted_dir_names[k] in group_path[i]:
                out.append({"name": group_name[i],
                            "path": group_path[i],
                            "dir_name": sorted_dir_names[k]})

    return out


def walk_in_path(directory, path, sort):
    files_list = []
    for root, directories, files in os.walk(path + directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            rel_filepath = filepath.replace(path, "")
            dir_name = get_dir_name(rel_filepath)
            files_list.append({"name": filename, "path": rel_filepath, "dir_name": dir_name})

    if sort:
        return sort_files(files_list)
    else:
        return files_list


def get_dir_name(path: str):
    name = ""
    counter = len(path) - 1
    while counter > 0:
        if path[counter] == os.sep:
            counter -= 1
            while True:
                if (counter == -1) or (path[counter] == os.sep):
                    return name[::-1]
                name += path[counter]
                counter -= 1
        counter -= 1


def get_files_in_directory(directory, path, sort=False):
    if directory in get_dirs_in_path(path):
        return walk_in_path(directory, path, sort)
    else:
        return None
