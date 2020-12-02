from pprint import pprint
from explore import get_all_files
import re
import struct

colors = {}


RESET = '\033[0m'


def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)


def save_colors(found_colors):
    for color in found_colors:
        if color in colors:
            colors[color] += 1
        else:
            colors[color] = 1


def get_rgb_from_hex(hex_color_string):
    return struct.unpack('BBB', bytes.fromhex(hex_color_string[1:]))


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
                  if sorted_colors[key] > 1 and len(key) == 7][:10]

    for top_color in top_colors:
        r, g, b = get_rgb_from_hex(top_color)
        print(get_color_escape(r, g, b, background=True) + '  ' +
              RESET, top_color, sorted_colors[top_color])
