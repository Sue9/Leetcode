# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:32:20 2019

@author: Sue

216. Combination Sum III
"""

class Solution(object):
    def findCombination(self, k, n, start, c, res):
        
        if (k == 1) and (n >= start) and (n <= 9):
            c.append(n)
            res.append(c[:])
            c.pop()
            return
        
        if (k <= 1):
            return
        
        if (n < start):
            return
        
        #k > 1
        for i in range(start, min(9, n) + 1):
            
            c.append(i)
            newN = n - i
            self.findCombination(k-1, newN, i+1, c, res)
            c.pop()
            
            
        return
        
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        if(k <= 0) or (k > 9) or (n <= 0):
            return []
        
        #min solution
        minSum = sum([i for i in range(1,k)])
        if(minSum > n):
            return []
        
        #max solution
        maxSum = sum([(9-i) for i in range(k)])
        if(maxSum < n):
            return []
        
        
        # minSum >= n, which means there is at least one solution
        # k >= 1 & n >= 1
        res = list()
        c = list()
        self.findCombination(k, n, 1, c, res)
        return res
        