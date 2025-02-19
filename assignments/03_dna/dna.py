#!/usr/bin/env python3
"""
Author : Jonah Parnaby <JonahParnaby@arizona.edu>
Date   : 2025-02-11
Purpose: Input DNA sequence
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='Input DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    DNA = args.DNA.upper()

    a_count = DNA.count('A')
    c_count = DNA.count('C')
    g_count = DNA.count('G')
    t_count = DNA.count('T')

    print(a_count, c_count, g_count, t_count)

# --------------------------------------------------
if __name__ == '__main__':
    main()
