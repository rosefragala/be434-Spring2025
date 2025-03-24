#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-03-24
Purpose: Find common words in two files
"""

import argparse
import sys
from typing import TextIO, Set


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2',
                        )

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------


def get_words(filehandle: TextIO) -> Set[str]:
    """Return a set of words from a filehande"""
    words = set()
    for line in filehandle:
        words.update(line.split())
    return words


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words1 = get_words(args.FILE1)
    words2 = get_words(args.FILE2)

    common = sorted(words1 & words2)

    for word in common:
        print(f'{word}', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
