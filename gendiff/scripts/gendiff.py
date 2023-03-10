import argparse
from gendiff import generate_diff
from gendiff.formatters import stylish, plain, json

FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        choices=FORMATTERS.keys(),
                        help='set format of output')
    args = parser.parse_args()
    formatter = FORMATTERS[args.format]
    diff = generate_diff(args.first_file, args.second_file)
    print(formatter.format(diff))


if __name__ == '__main__':
    main()
