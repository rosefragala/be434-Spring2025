#!/usr/bin/env python3
"""
Author : Jonah Parnaby <Add your email>
Date   : 2025-01-30
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
                        description='Print greeting',
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                                        '--greeting',
                                        help='The greeting',
                                        metavar='str',
                                        type=str,
                                        default='Howdy')

    parser.add_argument('-n',
                                        '--name',
                                        help='Whom to greet',
                                        metavar='str',
                                        type=str,
                                        default='Stranger')
                    # you want to make this a boolean
    parser.add_argument('-e',
                                        '--excited',
                                        help='Include an exclamation point',
                                        action='store_true')


    return parser.parse_args()
# --------------------------------------------------
def main():


    args = get_args()
    g = args.greeting
    n = args.name
    e = args.excited

#Purpose: Say Howdy, Stranger.


    article = '!' if e else '.'
    print(g + ', ' + n + article)


# --------------------------------------------------
if __name__ == '__main__':
    main()
