"""
Given a file containing text. Complete using only default collections:
   1) Find 10 longest words consisting from largest amount of unique symbols
   2) Find the rarest symbol for document
   3) Count every punctuation char
   4) Count every non ascii char
   5) Find most common non ascii char for document
"""
import string
from typing import List
from collections import Counter
from string import punctuation
import codecs
import re


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Function that finds 10 longest words consisting from the largest amount of unique symbols"""
    text = ''
    with open(file_path, 'r') as f:
        text = codecs.decode(f.read(), 'unicode-escape')
    clean_text = ''
    l_ind = 0
    while l_ind < len(text):
        if text[l_ind:l_ind + 2] == '-\n':
            clean_text += ''
            l_ind += 2
        elif text[l_ind] == ' ':
            clean_text += ' '
            l_ind += 1
        elif text[l_ind] == '-' and str.isalpha(text[l_ind + 1]):
            clean_text += '-'
            l_ind += 1
        elif str.isalpha(text[l_ind]):
            clean_text += text[l_ind]
            l_ind += 1
        elif text[l_ind] == '\n':
            clean_text += ' '
            l_ind += 1
        else:
            clean_text += ''
            l_ind += 1
    diverse_words_tuples = [(w, len(set(w))) for w in set(clean_text.split())]
    diverse_words_tuples = sorted(diverse_words_tuples, key=lambda tup: (tup[1], len(tup[0])), reverse=True)
    return [w[0] for w in diverse_words_tuples[:10]]


def get_rarest_char(file_path: str) -> str:
    """Function that find the rarest char in file"""
    text = ''
    res = None
    with open(file_path, 'r') as f:
        text = codecs.decode(f.read(), 'unicode-escape')
        chars = Counter([i for i in text])
        res = min(chars, key=chars.get)
    return res


def count_punctuation_chars(file_path: str) -> int:
    """Function that count punctuation symbols"""
    text = ''
    count = 0
    with open(file_path, 'r') as f:
        text = codecs.decode(f.read(), 'unicode-escape')
        for l in text:
            if l in punctuation:
                count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """Function that find non-ascii chars (unicode) using Regular Expressions"""
    pattern = r'\\u[0-9|a-f]{4}'
    text = ''
    with open(file_path, 'r') as f:
        text = f.read()
    res = re.findall(pattern, text)
    return len(res)


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Function that find the most common non ascii char using regexp and Counter"""
    pattern = r'\\u[0-9|a-f]{4}'
    text = ''
    count_unicode = ''
    with open(file_path, 'r') as f:
        text = f.read()
        unicode_symbols = re.findall(pattern, text)
        count_unicode = Counter([i for i in unicode_symbols])
    return codecs.decode(max(count_unicode, key=count_unicode.get), 'unicode-escape')
