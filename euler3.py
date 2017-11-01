"""
Project Euler Problem #3

Find the largest prime factor of 600851475143
"""
import math


def factor(number):
    ''' Finds the factors of a given number (works)'''
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if (number) % i == 0:
            factors.append(i)
            factors.append(number/i)
    return factors

'''
def factor(number):
    # Finds the odd factors of a given number
    factors = []
    counts = []
    tick = 1
    while tick < number:
        if tick % 2 == 0:
            if tick % 3 == 0:
                if tick % 5 == 0:
                    counts.append(tick)
        tick += 1
    for i in counts:
        if number % i == 0:
            factors.append(i)
    return factors
'''
'''
To find a prime factorial (by brute force)

Sieve of Eratosthenes

 Input: an integer n > 1.

 Let A be an array of Boolean values, indexed by integers 2 to n,
 initially all set to true.

 for i = 2, 3, 4, ..., not exceeding sqrt(n):
   if A[i] is true:
     for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
       A[j] := false.

 Output: all i such that A[i] is true.
 '''


def factor_dict(number):
    ''' creates a dictionary of factors that are all "True".'''
    my_dict = {}
    for i in number:
        my_dict[i] = True
    return my_dict


def prime_factor(number):
    ''' Evaluates dictionary keys to see if they are prime numbers '''
    factors = factor(number)
    true_list = factor_dict(factors)
    for k in true_list:
        for i in range(2, (int(math.sqrt(number) + 1))):
            if k != i:
                if k % i == 0:
                    true_list[k] = False
    return true_list

def prime_list(number):
    ''' returns all key in a dict with a True value'''
    factors = prime_factor(number)
    final_list = []
    for k in factors:
        if factors[k] == True:
            final_list.append(k)
    return final_list


print prime_factor(600851475143)
print prime_list(600851475143)
