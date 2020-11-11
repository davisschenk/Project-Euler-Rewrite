from itertools import permutations

from problem import Problem
from utils.primes import simple_is_prime


class PandigitalPrime(Problem, name="Pandigital prime", expected=7652413):
    @Problem.solution()
    def brute_force(self):
        for i in (7, 4):  # all other lengths of n are divisible by 3
            digits = reversed("123456789"[:i])
            for j in permutations(digits):
                j = int(''.join(j))
                if simple_is_prime(j):
                    return j
