# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:35:54 2018

@author: Sue

026 Remove Duplicates from Sorted Array
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        left  = 0
        right = 1
        
        while right < len(nums):
            if nums[right] not in nums[0:left+1]:
                right += 1
                left  += 1
            else:
                
        
