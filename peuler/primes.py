__author__ = 'Cam'

import math


def sieve(bound):
    if bound < 2:
        raise ValueError("Bound must be 2 or greater.")
    sieve_list = [True for _ in xrange(bound + 1)]
    primes = []
    for i in xrange(2, bound + 1):
        if not sieve_list[i]:
            continue
        primes.append(i)
        for j in xrange(2 * i, bound + 1, i):
            sieve_list[j] = False
    return primes


def factorize(n):
    if n < 1:
        raise ValueError("n must be positive.")
    primes = sieve(int(n ** .5 + 1))
    factors = []
    p_len = len(primes)
    i = 0
    while i < p_len:
        p = primes[i]
        if n % p == 0:
            factors.append(p)
            n /= p
        else:
            i += 1
    if n != 1:
        factors.append(n)
    return factors


def approx_nth_prime(n):
    if n < 1:
        raise ValueError("n must be greater than 0.")
    return n * math.log(n, math.e)


def nth_prime(n):
    if n < 1:
        raise ValueError("n must be greater than 0")
    bound = max(2, int(approx_nth_prime(n) + 1))
    primes = sieve(bound)
    i = n
    while len(primes) < n:
        i += 1
        bound = approx_nth_prime(i)
        primes = sieve(int(bound+1))
    return primes[n-1]


def string_rotate(s):
    if len(s) == 0:
        return ""
    return s[1:]+s[0]


def int_rotations(n):
    s = str(n)
    rots = [int(s)]
    for _ in xrange(int(math.floor(math.log10(n)))):
        s = string_rotate(s)
        rots.append(int(s))
    return rots


def is_circular_prime(prime_set, n):
    if all((r in prime_set) for r in int_rotations(n)):
        return True
    return False
