# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:49:45 2018

@author: zhaoxu

268 Missing Number
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #solution 4: dictionary, key-value
        nums.sort()
        
        for key,value in enumerate(nums):
            if key != value:
                return key
        else:
            return key+1
        
        
        """
        
        #solution 3: bit operation
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i ^ nums[ i ])
        return res
        """
        
        
        """
        #solution 2: using arithmetic formula
        sumN = int((len(nums) + 1) * len(nums) / 2)
        return sumN - sum(nums)
        """
        
        
        
        """
        solution 1: using for-loop
            
            
            
        l = len(nums)
        s = 0
        
        for i in range(l):
            s += (i+1) - nums[i]
        return s    
            
        """
        