#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-03-02
Purpose: Compute GC content in sequences
"""

import argparse
import sys


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input sequence file')

    return parser.parse_args()


# --------------------------------------------------


def gc_content(dna):
    """Calculate GC content of a sequence"""
    gc_count = sum(1 for base in dna if base in 'GC')
    return (gc_count / len(dna)) * 100 if dna else 0


# --------------------------------------------------


def main():
    """Process the input file and compute GC content"""

    args = get_args()
    dna = {}
    seq_id = None

    for line in args.file:
        line = line.strip()
        if line.startswith('>'):
            seq_id = line[1:]
            print(f"Processing sequence: {seq_id}")
            dna[seq_id] = ''
        elif seq_id:
            dna[seq_id] += line

    max_gc_id = None
    max_gc_value = -1

    for seq_id, seq in dna.items():
        gc_val = gc_content(seq)
        if gc_val > max_gc_value:
            max_gc_id, max_gc_value = seq_id, gc_val

    if max_gc_id is not None:
        print(f'{max_gc_id} {max_gc_value:.6f}')
    else:
        print("No valid sequences found.", file=sys.stderr)


# --------------------------------------------------
if __name__ == '__main__':
    main()
