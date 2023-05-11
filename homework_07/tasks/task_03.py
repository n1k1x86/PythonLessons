"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
#>>> universal_file_counter(test_dir, "txt")
6
#>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import string
from pathlib import Path
from typing import Optional, Callable

from os import listdir
from os.path import join


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    all_files = [f for f in listdir(dir_path) if f.endswith(file_extension)]
    count = 0
    for file in all_files:
        with open(join(dir_path, file), 'r') as f:
            text = f.read().translate(str.maketrans('', '', string.punctuation))
            if tokenizer:
                count += len(tokenizer(text))
            else:
                count += text.count('\n')
    return count
