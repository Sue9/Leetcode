# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:52:24 2019

@author: Sue

075. Sort Colors
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #0 in [0..zero]
        #2 in [two..len(nums)-1]
        #1 in [zero+1..two-1]
        zero = -1
        two = len(nums)
        e = 0
        
        while (e < two):
            if nums[e] == 1:
                e += 1
            elif nums[e] == 2:
                two -= 1
                nums[e], nums[two] = nums[two], nums[e]
            else:
                #nums[e] == 0
                zero += 1
                nums[e], nums[zero] = nums[zero], nums[e]
                e += 1
                
                