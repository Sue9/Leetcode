# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:07:54 2018

@author: zhaoxu

238 Product of Array Except Self
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if(len(nums) <= 1):
            return nums
        
        
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
            
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res