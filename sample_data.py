#!/usr/bin/env python3
import json
import os


def get_formatted_directory(db_type):
    formatted_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "formatted_data")
    ensure_directory(formatted_directory)

    formatted_db_type_directory = os.path.join(formatted_directory, db_type)
    ensure_directory(formatted_db_type_directory)

    return formatted_db_type_directory


def format_mongo_js(file_path):
    formatted_directory = get_formatted_directory("mongo_js")
    data = []
    with open(file_path) as data_file:
        for each_line in data_file.readlines():
            json_object = json.loads(each_line.strip())
            json_object.pop("_id")
            data.append(json_object)

    file_name = f"{file_path.split('/')[-1].split('.')[0]}.js"
    with open(os.path.join(formatted_directory, file_name), 'w') as formatted_data_file:
        formatted_data_file.write("var data = ")
        json.dump(data, formatted_data_file)
        formatted_data_file.write(";")


def ensure_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def format_json(file_path):
    if not file_path.endswith(".json"):
        return
    format_mongo_js(file_path)


def formatter():
    data_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "raw_data")
    for each_file in os.listdir(data_directory):
        file_path = os.path.join(data_directory, each_file)
        if not os.path.isfile(file_path):
            continue

        format_json(file_path)


if __name__ == '__main__':
    formatter()
