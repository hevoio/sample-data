#!/usr/bin/env python3
import json
import os
import sys


def json_cleaner(file_path):
    if not file_path.endswith(".json"):
        return

    with open(file_path) as data_file:
        data = json.load(data_file)

    with open(file_path, 'w') as data_file:
        for each_line in data:
            json.dump(each_line, data_file)
            data_file.write("\n")


def array_to_jsonl():
    data_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "raw_data")
    json_cleaner(os.path.join(data_directory, sys.argv[1]))


if __name__ == '__main__':
    array_to_jsonl()
