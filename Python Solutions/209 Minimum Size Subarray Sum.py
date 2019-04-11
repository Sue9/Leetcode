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
        
        l = 0
        r = l+1
        tempSum = nums[l] + nums[r]
        hasResult = False
        res = len(nums)
        
        while (l < len(nums) - 1) and (r < len(nums)):
            print("l = ", l, " r = ",r)
            if (tempSum < s):
                r += 1
                if (r > len(nums) - 1):
                    break
                tempSum += nums[r]
            elif (tempSum > s):
                tempSum -= nums[l]
                l += 1
            else: # tempSum == s
                res = min(res, r - l + 1)
                hasResult = True
                
                tempSum -= nums[l]
                l += 1
                r += 1
                if (r > len(nums) - 1):
                    print("Break")
                    break
                tempSum += nums[r]
        
        if (hasResult):
            return res
        else:
            return 0
                