# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:52:07 2019

@author: Sue

279. Perfect Squares
"""
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n <= 0):
            return 0
        
        if (n == 2):
            return 2
        
        #check if it's perfect square number
        if (int(math.sqrt(n)) == math.sqrt(n)):
            return 1
        
        memo = [1 for i in range(n+1)]
        memo[2] = 2
        for i in range(3, n+1):
            si = int(math.sqrt(i))
            if (si == math.sqrt(i)):
                memo[i] = 1
            else:
                minI = 2 * i
                for s in range(1, si+1):
                    numI = memo[i - s ** 2] + 1
                    if numI < minI:
                        minI = numI
                memo[i] = minI
            print("i = ", i, " memo[i] = ", memo[i])
        
        return memo[n]
        