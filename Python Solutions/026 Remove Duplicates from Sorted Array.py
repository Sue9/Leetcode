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
        
        cnt = 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[cnt]:
                cnt += 1
                nums[cnt] = nums[i]
        return cnt+1
        
        
                
                
        
