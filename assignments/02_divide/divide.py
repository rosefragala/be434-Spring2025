#!/usr/bin/env python3
"""
Author :Jonah Parnaby <Jonahparnaby@arizona.edu>
Date   : 2025-02-06
Purpose: Divide two numbers
"""

import argparse
import sys
import math

#from sre_constants import FAILURE


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""


    parser = argparse.ArgumentParser(
        description='Divide two numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('num1',
        metavar='int',
        type=int,
        help='First integer')

    parser.add_argument('num2',
        metavar='int',
        type=int,
        help='Second integer')

    return parser.parse_args()
# --------------------------------------------------
def main():
    """Main function to divide"""
    args = get_args()
    a = args.num1
    b = args.num2
    
    if b == 0:
        print('Usage: Cannot divide by zero, dum-dum!')
        sys.exit(1)
        
    result = a / b
   
    result = math.floor(a / b)
        

    print(f"{a} / {b} = {result}")
  
# --------------------------------------------------
if __name__ == '__main__':
    main()
