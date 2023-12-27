#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    if len(arr) <= 0:
        return 0
    else:
        first = arr[0]
        total = 0
        for i in range(1, len(arr)):
            if arr[i] == first:
                total = arr[i] + total
                continue
            else:
                size = len(arr)
                max_sum = 0
                min_sum = 0
                
                max_val = max(arr)
                min_val = min(arr)
                
                for i in range(size):
                    if arr[i] != min_val:
                        max_sum = arr[i] + max_sum
            
                for i in range(size):
                    if arr[i] != max_val:
                        min_sum = arr[i] + min_sum
                        
                print(min_sum, max_sum)
                return
            
        print(total, total)
        return
            
                
            
    
            


