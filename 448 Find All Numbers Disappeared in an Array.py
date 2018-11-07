# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:09:18 2018

@author: zhaoxu


448 Find All Numbers Disappeared in an Array
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        
        for i in range(len(nums)):
            tmpInd = abs(nums[i]) - 1
            if nums[tmpInd] > 0:
                nums[tmpInd] = -nums[tmpInd]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res
        
        """
        
        #Fail: Time limit exceed
        
        
        res = []
        
        for i in range(1, len(nums)+1):
            if i not in nums:
                res.append(i)
        
        return res
    
        """