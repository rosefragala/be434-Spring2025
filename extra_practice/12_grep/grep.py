#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-04-25
Purpose: Search for patterns in txt files
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    flags = re.IGNORECASE if args.insensitive else 0
    regex = re.compile(args.pattern, flags)

    multiple_files = len(args.files) > 1

    for fh in args.files:
        for line in fh:
            if regex.search(line):
                if multiple_files:
                    print(f'{fh.name}:{line.rstrip()}', file=args.outfile)
                else:
                    print(line.rstrip(), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
