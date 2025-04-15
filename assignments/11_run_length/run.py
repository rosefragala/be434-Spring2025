#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-04-15
Purpose: Run-length encoding
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
    )
    parser.add_argument('str',
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        with open(args.str, encoding='utf-8') as f:
            args.str = f.read().rstrip()

    return args


# --------------------------------------------------
def rle(seq):
    """Create RLE from a sequence"""
    if not seq:
        return ''
    result = []
    count = 1
    prev = seq[0]

    for char in seq[1:]:
        if char == prev:
            count += 1
        else:
            result.append(prev + (str(count) if count > 1 else ''))
            prev = char
            count = 1
    result.append(prev + (str(count) if count > 1 else ''))
    return ''.join(result)


# --------------------------------------------------
def test_rle():
    """Test rle"""
    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
def main():
    """make jazz noise here"""
    args = get_args()
    for seq in args.str.splitlines():
        print(rle(seq))


if __name__ == '__main__':
    main()
