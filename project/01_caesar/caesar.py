#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-04-29
Purpose: encode or decode caeser shift
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='caesar shift',
        )

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag (default: False)',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file (default: std.out)',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def build_substitution_table(shift, decode=False):
    """Build a substition table for encoding and decoding"""

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted = alpha[shift:] + alpha[:shift]

    if decode:
        return dict(zip(shifted, alpha))
    return dict(zip(alpha, shifted))


# --------------------------------------------------
def caesar(text, subs):
    """Apply Caesar shift using substitution table"""

    result = ''
    for char in text:
        if char.upper() in subs and char.isalpha():
            result += subs[char.upper()]
        else:
            result += char
    return result


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.FILE
    shift = args.number % 26
    decode = args.decode
    outfile = args.outfile

    subs = build_substitution_table(shift, decode)

    for line in file:
        transformed = caesar(line.strip(), subs)
        print(transformed.upper(), file=outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
