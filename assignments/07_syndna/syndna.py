#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-03-19
Purpose: Create synthetic DNA/RNA sequences
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--outfile',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default='out.fa',
                        help='Output filename')

    parser.add_argument('-t', '--seqtype',
                        metavar='str',
                        type=str,
                        choices=['dna', 'rna'],
                        default='dna',
                        help='DNA or RNA')

    parser.add_argument('-n', '--numseqs',
                        metavar='int',
                        type=int,
                        default=10,
                        help='Number of sequences to create')

    parser.add_argument('-m', '--minlen',
                        metavar='int',
                        type=int,
                        default=50,
                        help='Minimum length')

    parser.add_argument('-x', '--maxlen',
                        metavar='int',
                        type=int,
                        default=75,
                        help='Maximum length')

    parser.add_argument('-p', '--pctgc',
                        metavar='float',
                        type=float,
                        default=0.5,
                        help='Percent GC')

    parser.add_argument('-s', '--seed',
                        metavar='int',
                        type=int,
                        default=None,
                        help='Random seed')

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args


# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""
    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)

    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for i in range(1, args.numseqs + 1):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = ''.join(random.sample(pool, seq_len))
        args.outfile.write(f'>{i}\n{seq}\n')

    args.outfile.close()
    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} '
          f'sequences to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
