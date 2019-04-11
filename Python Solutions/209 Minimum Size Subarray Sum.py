# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:25:03 2019

@author: Sue

209. Minimum Size Subarray Sum
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if (nums == []):
            return 0
        
        if (len(nums) == 1):
            return int(nums[0] >= s)
        
        l = 0
        r = l
        tempSum = nums[l]
        hasResult = False
        res = len(nums)
        
        while (l < len(nums)) and (r < len(nums)):
            
            if (tempSum < s):
                r += 1
                if (r > len(nums) - 1):
                    break
                tempSum += nums[r]
            
            else: # tempSum >= s
                res = min(res, r - l + 1)
                hasResult = True
                tempSum -= nums[l]
                l += 1
                
        
        if (hasResult):
            return res
        else:
            return 0
                