import os
import pathlib
import requests



def read_file(path: str | pathlib.Path):
    path = pathlib.Path(path)

    try:
        with open(path.resolve().as_posix()) as f:
            data = f.read()
    except (Exception,):
        print('Err - except Exception: try: with open(path.absolute().as_posix()) ')
        return

    return data


def write_file(path: str | pathlib.Path, data, mode='w+') -> pathlib.Path | None:
    path = pathlib.Path(path)
    try:
        with open(path.resolve().as_posix(), mode) as f:
            f.write(data)
    except (Exception,):
        print('Err.', 'write_file: try: with open()')
        return

    return path


def walk_files(path: str | pathlib.Path) -> list[pathlib.Path]:
    path = pathlib.Path(path)
    data = []
    for root, dirs, files in os.walk(path.as_posix(), topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            data.append(file_path)

    all_files = [pathlib.Path(file) for file in data]
    return all_files


def wget(url):
    r = requests.get(url, allow_redirects=True)
    return r.content.decode('utf-8')



