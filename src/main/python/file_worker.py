import os
from subprocess import Popen
from datetime import datetime

from pytz import utc
from natsort import natsorted

# from src.main.python.config.config_dataclass import ConfigData
import src.main.python.enums as enums


images_formats = [".jpg", ".jpeg", ".png"]


def __get_dirs_in_path(path):
    files_in_dir = os.listdir(path)
    out = []
    for each in files_in_dir:
        if os.path.isdir(path + each):
            out.append(each)
    return out


def get_dirs_in_path(path):
    dirs = __get_dirs_in_path(path)
    files_list = []
    for each in dirs:
        files_list.append({"name": each, "path": "image.png"})
    return files_list


def get_dirs_in_path_with_image(path):
    dirs = __get_dirs_in_path(path)
    files_list = []
    for each in dirs:
        try:
            flag = False
            for root, directories, files in os.walk(path + each + os.sep):
                if flag:
                    break
                for filename in files:
                    if flag:
                        break
                    filepath = os.path.join(root, filename)
                    rel_filepath = filepath.replace(path, "")
                    for sign in images_formats:
                        if filename.endswith(sign):
                            files_list.append({"name": each, "path": rel_filepath})
                            flag = True
                            break
            if not flag:
                files_list.append({"name": each, "path": "image.png"})
        except Exception as e:
            print(e)
    return files_list


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
            if sorted_names[i] == get_file_name(sorted_paths[j]):
                group_name.append(sorted_names[i])
                group_path.append(sorted_paths[j])

    for k in range(0, len(sorted_dir_names)):
        for i in range(0, len(group_path)):
            if sorted_dir_names[k] in group_path[i]:
                out.append({"name": group_name[i],
                            "path": group_path[i],
                            "dir_name": sorted_dir_names[k]})

    return out


def sort_files_natural(files):
    sorted_names = []
    sorted_paths = []
    out = []

    for each in files:
        sorted_names.append(each.get("name"))
        sorted_paths.append(each.get("path"))

    sorted_names = natsorted(sorted_names)

    for i in range(0, len(sorted_names)):
        for j in range(0, len(sorted_paths)):
            if sorted_names[i] == get_file_name(sorted_paths[j]):
                out.append({"name": sorted_names[i], "path": sorted_paths[j]})

    return out


def walk_in_path(directory, path, sort, sort_type):
    files_list = []
    for root, directories, files in os.walk(path + directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            rel_filepath = filepath.replace(path, "")
            dir_name = get_dir_name(rel_filepath)
            files_list.append({"name": filename, "path": rel_filepath, "dir_name": dir_name})

    if sort:
        if sort_type == 0:
            return sort_files(files_list)
        else:
            return sort_files_natural(files_list)
    else:
        return files_list


def get_file_name(path: str):
    name = ""
    for i in range(len(path) - 1, 0, -1):
        if path[i] == os.sep:
            return name[::-1]
        name += path[i]


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


def get_files_in_directory(directory, path, sort=False, sort_type=0):
    if directory in __get_dirs_in_path(path):
        return walk_in_path(directory, path, sort, sort_type)
    else:
        return None


def define_parser(item: dict):
    url, parser_type, action = list(item.values())
    if ((parser_type == enums.ParserTypeEnum.youtube.value) or
            (parser_type == enums.ParserTypeEnum.with_headers.value)):
        try:
            Popen(f"cd multi_parser && python3 -m src.main -p {parser_type} -a {action} -u '{url}'", shell=True)
        except Exception as e:
            print(e)
            return e
    else:
        return "Something Wrong: " + str(item)

    return item


# def get_now_time_formated() -> datetime:
#     now_time = datetime.now(utc)
#     # TODO optimize
#     formated_time = now_time.strftime(ConfigData.date_format)
#     return datetime.strptime(formated_time, ConfigData.date_format)

def get_now_time() -> datetime:
    # return datetime.now(utc)
    return datetime.now()
