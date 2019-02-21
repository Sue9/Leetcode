# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:15:37 2019

@author: Sue

77. Combinations
"""

class Solution(object):
    #Solution 2: optimisation: prune on for loop
    def generateCombination(self, n, k, start, c, res):
        """
        :type n: int #this is the end
        :type k: int
        :type start: int
        :type c: List[int]
        :type res: List[List[int]]
        :rtype: void
        """
        #print("CALL RECURSION \t nums = ", nums, "\t choose how many: ", k, " c = ", c, " res = ",res)
        if(k == len(c)):
            res.append(c[:])
            return
        
        for i in range(start, n + 1):
            
            c.append(i)
            
            self.generateCombination(n, k, i+1, c, res)
            #print("inner res = ", res)
            
            c.pop()
            #print("after pop, c = ",c, " res = ", res)
        return
        
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        # check validation of n and k
        if (n < 0) or (k < 0) or (k > n):
            return []
                
        if (k == 0) and (n >= 0):
            return [[]]
        
        if (k == n):
            return [list(range(1, n+1))]
        
        res = []
        self.generateCombination(n, k, 1, [], res)
        return res
    
    
    """
    #Solution 1: designed myself
    
    def generateCombination(self, nums, k, c, res):
        
        #print("CALL RECURSION \t nums = ", nums, "\t choose how many: ", k, " c = ", c, " res = ",res)
        if(k == 0):
            #Leetcode complier does not recognise copy()
            #s = c.copy()
            s = c[:]
            res.append(s)
            return
        
        for i in range(len(nums)):
            #print("index i = ", i, " of nums : ", nums )
            
            c.append(nums[i])
            #print("c = ", c)
            self.generateCombination(nums[i+1:], k - 1, c, res)
            #print("inner res = ", res)
            
            c.pop()
            #print("after pop, c = ",c, " res = ", res)
        return
        
        
    def combine(self, n, k):
                
        # check validation of n
        if (n < 0):
            return []
        
        # check validation of k
        if (k < 0) or (k > n):
            return []
        
        if (k == 0) and (n >= 0):
            return [[]]
        
        nums = list(range(1, n+1))
        if (k == n):
            return [nums]
        
        res = []
        self.generateCombination(nums, k, [], res)
        return res
     """   