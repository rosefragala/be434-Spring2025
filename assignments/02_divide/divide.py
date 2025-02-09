#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-02-09
Purpose: To divide two required integer values.
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser = argparse.ArgumentParser(description= 'Divide two numbers')
    parser.add_argument('INT', type = int, nargs = 2, help = 'Numbers to divide')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Perform Integer Division"""

    args = get_args()
    num1, num2 = args.INT
    if num2 == 0:
        print('usage: divide.py [-h] INT INT', file=sys.stderr)
        print('Cannot divide by zero, dum-dum!', file=sys.stderr)
        sys.exit(1)

    result = num1 // num2
    print(f'{num1} / {num2} = {result}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
