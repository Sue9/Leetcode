# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:55:37 2019

@author: Sue

204. Count Primes
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n <= 2):
            return 0
        #n >= 3
        #sieve represents 0 to (n-1)
        sieve = [True] * n
        sieve[0] = False
        sieve[1] = False
             
        for i in range(2, int(n ** 0.5) + 1):
            if (sieve[i]):
                sieve[i*i : : i] = [False] * len(sieve[i*i : :i])
        
        return sum(sieve)        
    
        
    """
    #Time Limit Exceed
    def isPrime(self, n):
                for i in range(2, n):
            if (n % i == 0):
                return False
        return True
        
    def countPrimes(self, n):
                
        if (n <= 2):
            return 0
        else:
            count = 1
            for i in range(3, n):
                if self.isPrime(i):
                    count += 1
            return count
    """