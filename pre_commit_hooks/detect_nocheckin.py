import argparse
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Sequence


class BadFile(NamedTuple):
    filename: str


def check_file_for_nocheckin(
        filenames: Sequence[str],
) -> List[BadFile]:
    """Check if files contain @nocheckin.

    Return a list of all files containing @nocheckin found.
    """
    bad_files = []

    no_checkin_b = b'@nocheckin'
    for filename in filenames:
        with open(filename, 'rb') as content:
            text_body = content.read()
            # naively match the entire file, low chance of incorrect
            # collision
            if no_checkin_b in text_body:
                bad_files.append(BadFile(filename))
    return bad_files


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+', help='Filenames to run')

    args = parser.parse_args(argv)

    bad_filenames = check_file_for_nocheckin(args.filenames)
    if bad_filenames:
        for bad_file in bad_filenames:
            print(f'@nocheckin found in {bad_file.filename}')
        return 1
    else:
        return 0


if __name__ == '__main__':
    exit(main())
