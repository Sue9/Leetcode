# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:29:10 2019

@author: Sue

213. House Robber II
"""

class Solution(object):
    def robNoncyclic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        
        prev1 = prev2 = 0
        for n in nums:
            tmp = prev1
            prev1 = max(n+prev2, prev1)
            prev2 = tmp
        return prev1
        
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if(n == 0):
            return 0
        if(n == 1):
            return nums[0]
        
        option1 = nums[0] + self.robNoncyclic(nums[2:n-1])
        option2 = self.robNoncyclic(nums[1:])
        return max(option1, option2)