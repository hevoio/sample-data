#!/usr/bin/env python3
import json
import os


def clean_dict(dict_object):
    if isinstance(dict_object, dict):
        for each_key in list(dict_object.keys()):
            value = dict_object.pop(each_key)
            if isinstance(value, dict) or isinstance(value, list):
                clean_dict(value)

            if each_key[0] in ["$"]:
                dict_object[f"_{each_key}"] = value
            else:
                dict_object[each_key] = value
    elif isinstance(dict_object, list):
        for each_obj in dict_object:
            clean_dict(each_obj)


def json_cleaner(file_path):
    if not file_path.endswith(".json"):
        return

    clean_data = []
    with open(file_path) as data_file:
        for each_line in data_file.readlines():
            json_object = json.loads(each_line.strip())
            json_object.pop("_id", None)
            clean_dict(json_object)
            clean_data.append(json_object)

    with open(file_path, 'w') as data_file:
        for each_line in clean_data:
            json.dump(each_line, data_file)
            data_file.write("\n")


def data_cleaner():
    data_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "raw_data")
    for each_file in os.listdir(data_directory):
        file_path = os.path.join(data_directory, each_file)
        if not os.path.isfile(file_path):
            continue

        json_cleaner(file_path)


if __name__ == '__main__':
    data_cleaner()
