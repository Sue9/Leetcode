# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:05:16 2018

@author: zhaoxu

169. Majority Element
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[int(len(nums)/2)]
        
        
        
        """
        l = len(nums)
        if l <= 2:
            return nums[0]
        
        for i in range(int(l/2)+1):
#            print("i = ",i)
#            print("l/2 = " , l/2)
#            print("nums.count(nums[i]) = ", nums.count(nums[i]))
#            print("if? = ", nums.count(nums[i]) > (l/2))
            if nums.count(nums[i]) > (l/2):
                return nums[i]
        """