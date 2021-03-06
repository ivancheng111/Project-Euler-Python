""" Problem 5
Start: Sep/10/2021 10:25am
Finished: Sep/10/2021 1:05pm
"""

from math import isqrt, lcm

def primes_between(lower, upper):
    if lower <= 2:
        lower = 2
    if upper <= 2:
        return []
    is_prime = [True] * (upper+1)
    # mark out 0 and 1 as False
    is_prime[0] = is_prime[1] = False

    # if True, mark out its multiples
    for i in range(lower, isqrt(upper)+1):
        if is_prime[i]:
            for x in range(i*i, upper+1, i):
                is_prime[x] = False
    
    return [i for i in range(upper+1) if is_prime[i]]

def prime_factors(num) -> list:
    if num < 2:
        return []
    if num <= 3:
        return [num]
    factors = []

    while num % 2 == 0:
        factors.append(2)
        num //= 2
        if num == 1:
            return factors
    
    for i in range(3, isqrt(num)+1,2):
        while num % i == 0:
            factors.append(i)
            num //= i
        if num == 1:
            return factors
    factors.append(num)
    return factors

# alternative LONG way
def compute2(lower, upper):
    num_factors = []
    # get prime factors of numbers
    for i in reversed(range(lower, upper+1)):
        num_factors += [prime_factors(i)]
    
    mlt = []
    # find the highest occuring counts of prime p, exponentiate to get its value, and multiply everything
    for p in primes_between(lower, upper):
        max_occurance = max(e.count(p) for e in num_factors)
        mlt.append(p**max_occurance)
    prdct = 1
    for i in mlt:
        prdct*=i
    return prdct

def compute(lower, upper):
	ans = 1
    # same thing as getting lcm of all the numbers
	for i in range(lower, upper+1):
		ans = lcm(i, ans)
	return str(ans)

lower, upper = 1, 20
print(f"Smallest Number Divisible by Numbers Between {lower} and {upper} Is: {compute(lower, upper)}")