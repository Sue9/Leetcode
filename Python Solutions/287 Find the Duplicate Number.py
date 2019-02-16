# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:41:33 2018

@author: Sue


287 Find the Duplicate Number


https://blog.csdn.net/monkeyduck/article/details/50439840
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - sum(list(range(1,len(nums))))
        
    
        """
        #Fail: Time Limit Exceed
        for i in range(1, len(nums)):
            if nums.count(i) > 1:
                return i
                
        """