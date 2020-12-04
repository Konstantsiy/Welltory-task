import glob
import json
import os
import logging
import jsonschema
from jsonschema import validate

logging.basicConfig(filename='C:\\Users\\Home\\PycharmProjects\\task\\data\\logfile.log', level=logging.ERROR)

files = []
files_data = []

file_name_data = {}


def get_schemes():
    schemes = []
    os.chdir('D:\\task\\task_folder\\schema')
    for f in glob.glob('*.schema'):
        with open(f, 'r') as file:
            schemes.append(json.load(file))
    return schemes


def get_json_data():
    os.chdir('D:\\task\\task_folder\\event')
    for f in glob.glob('*.json'):
        files.append(f)
        with open(f, 'r') as file:
            files_data.append(file.read())
    return files_data


def validate_json_data(json_data):
    execute_api_schemes = get_schemes()
    for scheme in execute_api_schemes:
        for entry in zip(json_data, files):
            try:
                validate(instance=entry[0], schema=scheme)
            except jsonschema.exceptions.ValidationError as err:
                s = err.message
                logging.error("\n\t\tFile: " + entry[1] + "\n\t\tMessage: " + s[s.find(':') + 1:] + "\n---------------------------")


json_data_from_files = []

for data in get_json_data():
    json_data_from_files.append(json.loads(data))

validate_json_data(json_data_from_files)
