import argparse
import ast
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable
from typing import Mapping
from typing import MutableMapping
from typing import Optional
from typing import Sequence
import sys
from typing import Tuple

def check_execution_order(content: Mapping[str, object], file_name: str) -> None:
    execution_count = 0
    code_cells = content['cells']

    ret = 0
    for cell in code_cells:
        if cell['cell_type'] != 'code':
            continue
        new_execution_count = cell['execution_count']
        if new_execution_count is not None and not new_execution_count > execution_count:
            sys.stdout.write(f'Cell {new_execution_count} comes after {execution_count} in file \'{file_name}\'\n')
            ret = 1
        if new_execution_count is not None:
            execution_count = new_execution_count
    return ret

def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    args = parser.parse_args(argv)

    ret = 0
    for file in args.files:
        with open(file) as fd:
            content = json.load(fd)
        ret = ret or check_execution_order( content, file)
    return ret


if __name__ == '__main__':
    exit(main())
