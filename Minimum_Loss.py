#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    a=max(price)
    for i in range(len(price)):
        for j in range(i,len(price)):
            if(i!=j):
                b=price[i]-price[j]
                if(b<a and b>=0):
                    a=b
    return a
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
