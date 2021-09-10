""" Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Start: Sep/04/2021 12:30am
Finished: Sep/04/2021 6:00pm
"""
from itertools import repeat

# sieve of eratosthenes
def nth_prime(nth):
    primes = [2, 3, 5, 7]
    end_segment = 1
    extend_at_most_n_segments_target = 10

    while len(primes) < nth:
        k = end_segment
        n = min(extend_at_most_n_segments_target, len(primes) - 1 - k)
        p, q = primes[k], primes[k + n]
        segment = range(p * p, q * q)
        segment_min = min(segment)
        segment_len = len(segment)
        is_prime = [True] * segment_len

        for i in range(k + n):
            pk = primes[i]
            start = segment_min + ((pk - (segment_min % pk) % pk))
            is_prime[start - segment_min::pk] = repeat(False, len(range(start - segment_min, segment_len, pk)))

        primes.extend([x for x, is_prime in zip(segment, is_prime) if is_prime])
        end_segment += n
    
    return primes[nth-1]

n = int(input("Nth Prime to Find: "))
print(f"Prime: {nth_prime(n)}")