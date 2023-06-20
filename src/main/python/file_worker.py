import os
import subprocess
import json


def get_dirs_in_path(path):
    return os.listdir(path)


def ethkey(eth):
    """Split an ethernet device name between text and digit groups as int,
    allowing consistent sorting of interfaces.

    Usage: `sorted(if_list, key=ethkey)`

    :param eth: Value to sort
    :type eth: str
    :return: List of str's (even indexes) and int's (odd indexes) to compare
    :rtype: list
    """

    keys = []
    if not eth:
        # If eth is a string it's empty, just return blank list
        return keys

    # Start with the first character already in last
    last, eth = eth[0], eth[1:]
    # If last is int we start at offset 1
    if last.isdigit():
        keys.append('')

    for i in eth:
        if i.isdigit() is last.isdigit():
            # Keep accumulating same type chars
            last += i
        else:
            # Save and restart next round
            try:
                int(last)
                keys.append(int(last) if last.isdigit() else last)
                last = i
            except:
                keys.append(str(last) if last.isdigit() else last)
                last = i

    # Save final round and return
    keys.append(int(last) if last.isdigit() else last)
    return keys


def sort_dict_alph(dictionary: dict):
    keys_sorted = []
    values_list = []
    out = {}
    for keys, values in dictionary.items():
        keys_sorted.append(keys)
        values_list.append(values)
    keys_sorted = sorted(keys_sorted, key=ethkey)
    for i in range(0, len(keys_sorted)):
        for j in range(0, len(keys_sorted)):
            if keys_sorted[i] in values_list[j]:
                out.update({keys_sorted[i]: values_list[j]})
    # for keys, values in out.items():
    #     print(keys, ": ", values)
    return out


def walk_in_path(directory, path):
    # file_paths = []  # List which will store all of the full filepaths.
    # file_names = []
    files_dict = {}
    # Walk the tree.
    for root, directories, files in os.walk(path + directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            # file_paths.append(filepath)  # Add it to the list.
            # file_names.append(filename)
            rel_filepath = filepath.replace(path, "")
            files_dict.update({filename: rel_filepath})
    return sort_dict_alph(files_dict)


def generate_json(directory, path):
    files_dict = get_all_files_in_directory(directory, path)
    files_list = []
    for keys, values in files_dict.items():
        # audio = audio_duration(values)
        # files_list.append({"name": keys, "file": values, "duration": audio})
        # print(f"{audio}")
        files_list.append({"name": keys, "path": values})
    # return json.dumps(files_list)
    return files_list


def get_all_files_in_directory(directory, path):
    if directory in get_dirs_in_path(path):
        return walk_in_path(directory, path)
    else:
        return None


def audio_duration(path):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    time = float(result.stdout)
    mon, sec = divmod(time, 60)
    hr, mon = divmod(mon, 60)
    return ("%d:%02d:%02d" % (hr, mon, sec))
