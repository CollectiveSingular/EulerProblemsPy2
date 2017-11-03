'''
Euler Problem #5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

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

def sequence_multiply(range_max):
    ''' multiplies a series of numbers together from 1 to maximum'''
    count = range(1, range_max + 1)
    total = 1
    for i in count:
        total = total * i
    return total


def factor_eval(max_factor):
    ''' Evaluate list for each number from 1 to 20 '''
    proof = range(1, max_factor+1)
    count = sequence_multiply(max_factor)
    test = factor(count)
    while count != 1:
        if sorted(proof) != sorted(test):
            count -= 1
        else:
            return count

print factor_eval(20)
