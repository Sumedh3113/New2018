'''Mug it up'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def primeCheck(i, primes):
            if i < 2:
                return False

            if i % 2 == 0:
                return i == 2
            for p in primes:
                if i < p*p:
                    return True
                if i % p == 0:
                    return False

            return True

        primes = []

        for i in range(2,n):
            if primeCheck(i, primes):
                primes.append(i)

        return len(primes)