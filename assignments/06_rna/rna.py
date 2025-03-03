#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-03-03
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
import sys


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input DNA file')

    parser.add_argument('-o', '--outdir', '--out_dir',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    return parser.parse_args()


# --------------------------------------------------


def transcribe_dna(dna):
    """"Convert DNA Sequence to RNA"""
    return dna.replace('T', 'U').replace('t', 'u')


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir
    files = args.files

    missing_files = [file for file in files if not os.path.isfile(file)]

    if missing_files:
        print("Usage:", file=sys.stderr)
        print("  rna.py [-o DIR] FILE...", file=sys.stderr)
        for file in missing_files:
            print(f"No such file or directory: '{file}'", file=sys.stderr)
            sys.exit(1)

    os.makedirs(out_dir, exist_ok=True)

    num_sequences = 0
    num_files = 0

    for file in files:
        num_files += 1
        output_file = os.path.join(out_dir, os.path.basename(file))

        with open(file, 'r', encoding='utf-8') as infile, \
                open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                rna_seq = transcribe_dna(line.strip())
                outfile.write(rna_seq + '\n')
                num_sequences += 1

    sequence_word = "sequence" if num_sequences == 1 else "sequences"
    file_word = "file" if num_files == 1 else "files"

    print(
        f'Done, wrote {num_sequences} {sequence_word} '
        f'in {num_files} {file_word} to directory "{out_dir}".'
        )


# --------------------------------------------------
if __name__ == '__main__':
    main()
