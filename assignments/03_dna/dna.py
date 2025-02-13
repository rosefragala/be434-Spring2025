#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-02-13
Purpose: count tetranucleotide frequency
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input DNA sequence')
    return parser.parse_args()


# --------------------------------------------------


def count_nucleotides(dna):
    """Count tetranucleotide frequency"""
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    dna = dna.replace("\n", "").replace("\t", "").replace(" ", "")

    for nucleotide in dna:
        if nucleotide in counts:
            counts[nucleotide] += 1
        else:
            raise ValueError(
                f"Invalid character in DNA sequence: {nucleotide}")
    return counts


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.DNA.upper().strip()
    counts = count_nucleotides(dna)

    print(counts["A"], counts["C"], counts["G"], counts["T"])


# --------------------------------------------------
if __name__ == '__main__':
    main()
