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

def factor_dict(number):
    ''' creates a dictionary of factors that are all "True".'''
    my_dict = {}
    for i in number:
        my_dict[i] = True
    return my_dict

def factor_eval(max_factor):
    ''' Evaluate list for each number from 1 to 20 '''
    factors = range(1, max_factor+1)
    count = max_factor
    for i in factors:
        if count % i != 0:
            count += 1
        else:
            return count

print factor_eval(20)