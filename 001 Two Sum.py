# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:31:49 2018

@author: zhaoxu

001 Two Sum
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        twoInd = []
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums[i+1:]:
                twoInd = [i, nums[i+1:].index(target - nums[i])+i+1]
                return twoInd
        
        return twoInd
                

