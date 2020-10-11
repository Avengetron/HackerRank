#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    sum=0
    for element in ar:
        
        sum+= element
    return sum
if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    
    result = simpleArraySum(ar)

    print(result)
