#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    if len(arr) <= 0:
        return 0
    else:
        arr_len = len(arr)
        positive = 0
        negative = 0
        zero = 0
        for i in range(0, arr_len):
            if arr[i] > 0:
                positive = positive + 1
            if arr[i] < 0:
                negative = negative + 1
            if arr[i] == 0:
                zero = zero + 1
                
        ratio_pos = positive / arr_len
        ratio_neg = negative / arr_len
        ratio_zero = zero / arr_len
    
    print("positive:",ratio_pos)
    print("negative:",ratio_neg)
    print("zeroes:",ratio_zero)
    
    

x = [2,4,5,0,-1,-2]
plusMinus(x)
    
            
    
    
    

