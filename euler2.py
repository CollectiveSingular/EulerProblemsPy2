"""
Euler Problem #2

Find the sum of all even numbers in the Fibonacci sequence less than 4 Million
"""

def fib(list_end):
    q = [1, 2]
    while max(q) < list_end:
        x = q[-1] + q[-2]
        q.append(x)
    return q

def even(q):
    r = []
    for i in q:
        if i%2 == 0:
            r.append(i)
    return r

x = fib(4000000)

print x

y = even(x)

print sum(x)
