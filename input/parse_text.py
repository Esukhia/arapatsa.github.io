from pathlib import Path

from third_party.dictify import dictify_text


def recursive_process(in_path):
    in_path = Path(in_path)
    for f in in_path.rglob('*.txt'):
        process_file(f)


def process_file(filename):
    dump = filename.read_text()
    htmlfile = filename.parent / (filename.stem + '.html')
    htmlfile.write_text(dump)


if __name__ == '__main__':
    in_path = 'content'
    recursive_process(in_path)
