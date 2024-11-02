import pathlib
import json
import yaml


def parser(first_file_path, second_file_path):
    file_ext = pathlib.Path(first_file_path).suffix
    parser_mapping = {
        '.json': json.load,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }
    first_file_object = parser_mapping[file_ext](open(first_file_path))
    second_file_object = parser_mapping[file_ext](open(second_file_path))
    return first_file_object, second_file_object
