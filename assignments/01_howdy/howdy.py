#!/usr/bin/env python3
"""
Author : Rose Fragala <rosefragala@arizona.edu>
Date   : 2025-02-03
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Greetings and Howdy',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g', '--greeting',
                           help='The greeting',
                           metavar='str',
                           type=str,
                           default='Howdy')

    parser.add_argument('-n', '--name',
                           help='Whom to greet',
                           metavar='str',
                           type=str,
                           default='Stranger')

    parser.add_argument('-e', '--excited',
                           help='Include an exclamation point',
                           action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """To generate and print the greetings! (well, hopefully)"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    punctuation = '!' if args.excited else '.'
    print(f'{greeting}, {name}{punctuation}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
