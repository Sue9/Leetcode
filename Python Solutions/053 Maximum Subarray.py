# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:38:36 2018

@author: zhaoxu

053 Maximum Subarray

good solution explanation :
    1. https://blog.csdn.net/the__apollo/article/details/77367534
    2. https://www.cnblogs.com/en-heng/p/3970231.html
    3. https://blog.csdn.net/lengxiao1993/article/details/52303492
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        
        currentMax = nums[0]
        currentSum = nums[0]
        
        for i in nums[1:]:
            
            currentSum = max(i, currentSum + i)
            currentMax = max(currentSum, currentMax)

                
        return currentMax
        