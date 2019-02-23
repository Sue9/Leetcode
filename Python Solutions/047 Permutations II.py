# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 16:00:38 2019

@author: Sue

47. Permutations II
"""

class Solution(object):
    def generatePermutations(self, nums, k, c, res):
        """
        :type nums: List[int]
        :type k: int : select k elements
        :type index: int : choose from
        :type c: List[int] : current part of the result
        :rtype: List[List[int]]
        """
        if(k == 0):
            res.append(c[:])
            return
        
        distinctNum = list(set(nums))
        for i in range(len(distinctNum)):
            c.append(distinctNum[i])
            nextNum = nums[:]
            nextNum.remove(distinctNum[i])
            self.generatePermutations(nextNum, k-1, c, res)
            c.pop()
        return
            
        
        
        
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums) == 0):
            return []
        
        res = list()
        self.generatePermutations(nums, len(nums), [], res)
        
        return res
        
        
        