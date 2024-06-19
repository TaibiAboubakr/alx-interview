#!/usr/bin/python3
""" is Winner """

def isWinner(x, nums):
    """ isWinner(x, nums) """

    def sieve_of_eratosthenes(max_num):
        """ sieve_of_eratosthenes """
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        prime_counts = [0] * (max_num + 1)
        count = 0
        for i in range(2, max_num + 1):
            if is_prime[i]:
                count += 1
            prime_counts[i] = count
        return prime_counts, is_prime

    if x <= 0 or not nums:
        return None
    
    max_n = max(nums)
    prime_counts, is_prime = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            primes = []
            for i in range(2, n + 1):
                if is_prime[i]:
                    primes.append(i)
            if len(primes) % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
