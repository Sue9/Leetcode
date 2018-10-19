# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:54:14 2018

@author: zhaoxu

217 Contains Duplicate
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        return len(nums) != len(set(nums)) 
        """
        #time limit exceed
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
            
        return False
        """