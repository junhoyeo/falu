from pprint import pprint
from explore import get_all_files


if __name__ == '__main__':
    searching_paths = [file['path'] for file in get_all_files(
        '.') if not file['is_directory']]
    pprint(searching_paths)

    number_of_paths = len(searching_paths)
    print(number_of_paths)
