'''
Euler Problem #4

Find the largest palindrome which is a product of two two-digit numbers
'''



def palindrome_pairs(number):
    ''' create list of tuples that yield palindromes '''
    cog1 = range(1, number + 1)
    cog2 = range(1, number + 1)
    palindromes = []
    for i in cog1:
        for n in cog2:
            answer = i * n
            if str(answer) == reversed(str(answer)):
                palindromes.append(i, n)
    return palindromes

def max_tuple(tuples):
    ''' evaluate list for maximum values '''
    ls = palindrome_pairs(tuples)
    maximum = 0
    for a, b in ls:
        if a * b > maximum:
            maximum = a * b
    return maximum

print palindrome_pairs(99)
print max_tuple(99)
