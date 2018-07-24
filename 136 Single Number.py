# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:25:31 2018

@author: zhaoxu

136. Single Number
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        
        for i in nums:
            res ^= i
            
        return res
        
        
        """
        My solution 1, failed
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]

"""