'''
Euler Problem #5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math


def factor(number):
    ''' Finds the factors of a given number (works)'''
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if (number) % i == 0:
            factors.append(i)
            factors.append(number / i)
    return factors

''' Evaluate list for each number from 1 to 20 '''