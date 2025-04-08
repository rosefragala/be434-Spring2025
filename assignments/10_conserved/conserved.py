#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-04-08
Purpose: Show conserved bases in aligned sequences
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def read_sequences(filename):
    """Read sequences from a file"""
    with open(filename, encoding='utf-8') as fh:
        return [line.strip() for line in fh if line.strip()]


# --------------------------------------------------
def find_conserved(seqs):
    """Return string with '|' for conserved and 'X' for non-conserved bases"""
    length = len(seqs[0])
    result = []

    for i in range(length):
        chars = [seq[i] for seq in seqs]
        result.append('|' if all(base == chars[0] for base in chars) else 'X')

    return ''.join(result)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    filename = args.file

    if not os.path.isfile(filename):
        sys.exit(f"No such file or directory: '{filename}'")

    sequences = read_sequences(filename)

    if not sequences:
        sys.exit('No sequences found in file')

    if len(set(len(seq) for seq in sequences)) != 1:
        sys.exit('All sequences must be the same length')

    for seq in sequences:
        print(seq)

    print(find_conserved(sequences))


# --------------------------------------------------
if __name__ == '__main__':
    main()
