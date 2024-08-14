import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file'
    )

    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')

    args = parser.parse_args()

    print(f'Comparing {args.first_file} and {args.second_file}')


if __name__ == '__main__':
    main()
