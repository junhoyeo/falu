import os
import os.path


def get_ignored_files(target_path):
    ignored_files = []

    git_path = os.path.join(target_path, '.git')

    if os.path.exists(git_path):
        ignored_files.append('.git')

    gitignore_path = os.path.join(target_path, '.gitignore')

    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as gitignore_file:
            ignored_files += [line.strip()
                              for line in gitignore_file.readlines()]
    return ignored_files


def get_files_under_path(target_path):
    ignored_files = get_ignored_files(target_path)

    files_in_path = []

    def is_path_ignored(file_path):
        for ignored in ignored_files:
            try:
                if os.path.samefile(os.path.join(target_path, ignored), file_path):
                    return True
            except FileNotFoundError:
                pass
        return False

    for file_name in os.listdir(target_path):
        file_path = os.path.join(target_path, file_name)
        is_ignored = is_path_ignored(file_path)
        if is_ignored:
            continue
        files_in_path.append({
            'name': file_name,
            'path': file_path,
            'is_directory': not os.path.isfile(file_path)
        })

    return files_in_path


def get_all_files(target_path):
    files = get_files_under_path(target_path)
    all_paths = files.copy()

    for file_information in files:
        if file_information['is_directory']:
            all_paths += get_all_files(file_information['path'])
    return all_paths
