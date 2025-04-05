#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-04-05
Purpose: Filter delimited records based on a given value.
"""

import argparse
import csv
import re
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter delimited records based on a given value.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-f', '--file', required=True, help='Input file'
    )
    parser.add_argument(
        '-v', '--val', required=True, help='Value to filter by'
    )
    parser.add_argument(
        '-c', '--col', help='Column name to filter by'
    )
    parser.add_argument(
        '-o', '--outfile', default='out.csv',
        help='Output filename (default: out.csv)'
    )
    parser.add_argument(
        '-d', '--delimiter', default=',',
        help='Delimiter for the input file (default: ",")'
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Filter records based on user-defined criteria"""
    # Manually check for file existence before full parsing.
    for i, arg in enumerate(sys.argv):
        if arg in ['-f', '--file'] and i + 1 < len(sys.argv):
            file_arg = sys.argv[i + 1]
            if not os.path.isfile(file_arg):
                print(f"No such file or directory: '{file_arg}'",
                      file=sys.stderr)
                sys.exit(1)
            break

    args = get_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile, delimiter=args.delimiter)
            fieldnames = reader.fieldnames

            # Validate column name if specified.
            if args.col and args.col not in fieldnames:
                print(f'--col "{args.col}" not a valid column!',
                      file=sys.stderr)
                sys.exit(1)

            with open(args.outfile, 'w', newline='', encoding='utf-8') as ofi:
                writer = csv.DictWriter(ofi, fieldnames=fieldnames)
                writer.writeheader()

                # Prepare a case-insensitive regex pattern.
                search_for = re.compile(re.escape(args.val), re.IGNORECASE)

                num_written = 0
                for rec in reader:
                    text = (rec.get(args.col)
                            if args.col else ' '.join(rec.values()))
                    if search_for.search(text):
                        num_written += 1
                        writer.writerow(rec)

                print(
                    f"Done, wrote {num_written} to "
                    f'"{args.outfile}".'
                )

    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
