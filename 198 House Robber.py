# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:31:45 2018

@author: Sue

198 House Robber
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        odd  = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
        
        return max(even, odd)