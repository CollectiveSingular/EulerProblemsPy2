'''
Euler Problem #5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math

# The answer will be a multiple of 2520
# The list of evaluated numbers will step by 2520
# 20 = 2, 5, 10
# 18 = 3, 6, 9
# 16 = 2, 4, 8
# 15 = 3, 5
# 14 = 2, 7
# 12 = 2, 3, 4

factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

tally = xrange(2520, 536870912, 2520)

def factor_proof(count):
    for i in xrange(count, 999999999, count):
        if all(i % n == 0 for n in factors):
            return i
    return None
        
print factor_proof(2520)


'''
This whole bit is barking up the wrong tree, I think.  Some logic needs to be built into the front end for the memory to work properly.

def factor_dict(number):
    # creates a dictionary of factors that are all "True".
    my_dict = {}
    for i in number:
        my_dict[i] = True
    return my_dict


def prime_factor(number):
    # Evaluates dictionary keys to see if they are prime numbers
    factors = range(1, number + 1)
    true_list = factor_dict(factors)
    for k in true_list:
        for i in range(2, (int(math.sqrt(number) + 1))):
            if k != i:
                if k % i == 0:
                    true_list[k] = False
    return true_list

def prime_list(number):
    # returns all key in a dict with a True value
    factors = prime_factor(number)
    final_list = []
    for k in factors:
        if factors[k] == True:
            final_list.append(k)
    return final_list

def unprime_list(number):
    # returns all key in a dict with a False value
    factors = prime_factor(number)
    final_list = []
    for k in factors:
        if factors[k] == False:
            final_list.append(k)
    return final_list

def unprime_products(number):
    # Returns the products of a list 
    raw_list = unprime_list(number)
    cooked_list = 1
    for i in raw_list:
        cooked_list = cooked_list * i
    return cooked_list

def factor_render(number):
    # Multiplies a list of prime numbers with remainders of the unprime list
    fat = prime_list(number)
    count = unprime_products(number)
    for i in fat:
        count = count * i
    return count

def factor_proof(number):
    # Finds the factors of a given number (works)
    factors = []
    test_range = factor_render(number)
    for i in range(1, int(math.sqrt(test_range)) + 1):
        if (number) % i == 0:
            factors.append(i)
            factors.append(number / i)
    return sorted(factors)


def factor(number):
    # Finds the factors of a given number (works)
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if (number) % i == 0:
            factors.append(i)
            factors.append(number / i)
    return factors

print prime_list(20)
print unprime_list(20)
print factor_render(20)
print factor_proof(20)
'''
