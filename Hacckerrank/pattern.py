#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    # Write your code here.
    #
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j <= n - i):
                print(' ', end = '')
            else:
                print('#', end = '')    
        print()
if __name__ == '__main__':
    n = int(input())

    staircase(n)
