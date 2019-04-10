# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:31:45 2019

@author: Sue

080. Remove Duplicates from Sorted Array II
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums == []):
            return 0
        
        k = 0
        
        for i in range(len(nums)):
            
            if nums[0:k].count(nums[i]) < 2:
                if (k != i):
                    temp = nums[i]
                    nums[i] = nums[k]
                    nums[k] = temp
                    k += 1
                else: # k == i
                    
                    k += 1
            
        return k
                
                
