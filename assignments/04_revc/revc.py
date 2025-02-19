#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-02-19
Purpose: Print the reverse complement of a DNA sequence
"""


import argparse


COMPLEMENTS = str.maketrans("ACGTacgt", "TGCAtgca")


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input sequence or file')

    return parser.parse_args()


# --------------------------------------------------


def reverse_complement(dna: str) -> str:
    """Return the reverse complement of a DNA sequence"""
    return dna[::-1].translate(COMPLEMENTS)


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    input_data = args.DNA

    try:
        with open(input_data, 'rt', encoding='utf-8') as file:
            dna = file.read().strip()
    except FileNotFoundError:
        dna = input_data.strip()

    print(reverse_complement(dna))


# --------------------------------------------------
if __name__ == '__main__':
    main()
