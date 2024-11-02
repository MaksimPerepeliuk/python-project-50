import argparse
import json


def get_filepaths_cli():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    args = parser.parse_args()
    first_file_path, second_file_path = args.first_file, args.second_file
    print(f'Comparing {first_file_path} and {second_file_path}')
    return first_file_path, second_file_path


def generate_diff(obj1, obj2):
    items1 = obj1.items()
    items2 = obj2.items()
    diff_actions = {
        '  ': lambda items1, items2: set(items1) & set(items2),
        '- ': lambda items1, items2: set(items1) - set(items2),
        '+ ': lambda items1, items2: set(items2) - set(items1)
    }
    diff_items = []
    for diff_char, diff_func in diff_actions.items():
        diff_items = [*diff_items,
                      *[(diff_char, k, v)
                        for k, v in diff_func(items1, items2)]]
    diff_dict = {f'{c}{k}': v
                 for c, k, v in sorted(diff_items, key=lambda item: item[1])}
    return json.dumps(diff_dict, indent=2)


def main():
    first_file_path, second_file_path = get_filepaths_cli()
    first_file = json.load(open(first_file_path))
    second_file = json.load(open(second_file_path))
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
