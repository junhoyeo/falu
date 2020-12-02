from pprint import pprint
from explore import get_all_files
import re


if __name__ == '__main__':
    target_path = './pointing-app'

    searching_paths = [file['path'] for file in get_all_files(
        target_path) if not file['is_directory']]

    number_of_paths = len(searching_paths)
    print(number_of_paths)

    for path in searching_paths:
        with open(path, 'r') as searching_file:
            try:
                content = searching_file.read()
                findings = re.findall(
                    r'/#[0-9a-f]{8}|#[0-9a-f]{6}|#[0-9a-f]{4}|#[0-9a-f]{3}/ig', content)
                pprint(findings)
            except UnicodeDecodeError:
                continue
