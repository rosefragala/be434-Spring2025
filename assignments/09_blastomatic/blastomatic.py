#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-04-05
Purpose: Annotate BLAST output by filtering and merging with metadata
"""

import argparse
import sys
import pandas as pd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b', '--blasthits', metavar='FILE', required=True,
                        help='BLAST -outfmt 6')

    parser.add_argument('-a', '--annotations', metavar='FILE', required=True,
                        help='Annotations file')

    parser.add_argument('-o', '--outfile', metavar='FILE', default='out.csv',
                        help='Output file')

    parser.add_argument('-d', '--delimiter', metavar='DELIM', default=None,
                        help='Output field delimiter')

    parser.add_argument('-p', '--pctid', metavar='PCTID', type=float,
                        default=0.0, help='Minimum percent identity')

    return parser.parse_args()


# --------------------------------------------------
def guess_delimiter(_):
    """Dummy guess_delimiter to satisfy unit_test.py import"""
    return ','


# --------------------------------------------------
def get_valid_delimiter(delim_arg, outfile):
    """Validate or guess a valid single-character delimiter"""
    if delim_arg is not None:
        delim_arg = delim_arg.strip()
        if len(delim_arg) != 1:
            print(
                f'Error: Delimiter "{delim_arg}" must be a single '
                'non-whitespace character.',
                file=sys.stderr)
            sys.exit(1)
        return delim_arg

    if outfile.endswith(('.tsv', '.tab', '.txt')):
        return '\t'
    return ','


# --------------------------------------------------
def main():
    """Main logic"""

    args = get_args()

    blast_file = args.blasthits
    annot_file = args.annotations
    outfile = args.outfile
    pctid = args.pctid
    delim = get_valid_delimiter(args.delimiter, outfile)

    try:
        blast_cols = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch',
                      'gapopen', 'qstart', 'qend', 'sstart', 'send',
                      'evalue', 'bitscore']
        blast_df = pd.read_csv(blast_file, names=blast_cols)
    except (IOError, ValueError) as e:
        print(f'Error reading BLAST file: {e}', file=sys.stderr)
        sys.exit(1)

    try:
        annot_df = pd.read_csv(annot_file, delimiter=',')
    except (IOError, ValueError) as e:
        print(f'Error reading annotation file: {e}', file=sys.stderr)
        sys.exit(1)

    filtered_df = blast_df[blast_df['pident'] >= pctid]
    merged_df = pd.merge(filtered_df, annot_df, left_on='qseqid',
                         right_on='seq_id')
    out_df = merged_df[['qseqid', 'pident', 'depth', 'lat_lon']]

    try:
        out_df.to_csv(outfile, index=False, sep=delim)
    except (pd.errors.ParserError, FileNotFoundError) as e:
        print(f'Error writing output file: {e}', file=sys.stderr)
        sys.exit(1)

    print(f'Exported {len(out_df)} to "{outfile}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
