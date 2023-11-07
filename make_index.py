
from utils import write_file

import pathlib


def make_index():
    from utils import write_file

    import pathlib

    root = pathlib.Path.cwd()
    store = pathlib.Path(root.name)

    media_suffixes = [
        '.jpg',
        '.jpeg',
        '.mp4',
    ]

    media_files = list(filter(lambda file: file.suffix in media_suffixes, store.iterdir()))

    media_files = sorted(media_files, reverse=True)

    text_output = ''

    text_output += f'## {store.name}'

    text_output += '\n'
    text_output += '\n'

    link = f'https://www.instagram.com/{store.name}/'

    text_output += f'[{link}]({link})'

    text_output += '\n'
    text_output += '\n'

    text_output += f'### Media'

    text_output += '\n'
    text_output += '\n'

    for file in media_files:
        text_output += f'[{file.name}]({file})'
        text_output += '\n'
        text_output += '\n'

    write_file('index.md', text_output)


if __name__ == '__main__':
    make_index()
