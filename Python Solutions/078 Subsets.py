# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:00:59 2019

@author: Sue


78. Subsets
"""
class Solution(object):
    def findCombinations(self, nums, k, start, c, res):
        """
        :type nums: List[int]
        :type k: int 
        :type start: int: start index
        :type c： List[int]
        :rtype: List[List[int]]
        """
        if (k == len(c)):
            res.append(c[:])
            return
        
        for i in range(start, len(nums) - (k - len(c)) + 1):
            c.append(nums[i])
            self.findCombinations(nums, k, i+1, c, res)
            c.pop()
        return
            
            
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (nums == []):
            return [[]]
        
        res = list()
        
        # add subset having 0 element
        res.append([])
        
        # add subsets from having elements of 1 to n-1
        for k in range(1, len(nums)):
            c = list()
            # select k elements from nums[0:]
            self.findCombinations(nums, k, 0, c, res)
            
        # add subset having all elements
        res.append(nums)
        
        return res
            
        
