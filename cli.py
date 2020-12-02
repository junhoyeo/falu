from pprint import pprint
from explore import get_all_files
import re

colors = {}


def save_colors(found_colors):
    for color in found_colors:
        if color in colors:
            colors[color] += 1
        else:
            colors[color] = 1


if __name__ == '__main__':
    target_path = './pointing-app'

    searching_paths = [file['path'] for file in get_all_files(
        target_path) if not file['is_directory']]

    number_of_paths = len(searching_paths)
    print(f'🔍 {number_of_paths} files searched')

    for path in searching_paths:
        with open(path, 'r') as searching_file:
            try:
                content = searching_file.read()
                findings = re.findall(
                    r'/#[0-9a-f]{8}|#[0-9a-f]{6}|#[0-9a-f]{4}|#[0-9a-f]{3}/ig', content)
                save_colors(findings)
            except UnicodeDecodeError:
                continue

    sorted_colors = dict(
        sorted(colors.items(), key=lambda item: item[1], reverse=True))

    del colors

    top_colors = [key for key in sorted_colors.keys()
                  if sorted_colors[key] > 1][:10]

    pprint(top_colors)
