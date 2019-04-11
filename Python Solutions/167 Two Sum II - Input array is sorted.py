# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:18:11 2019

@author: Sue

167. Two Sum II - Input array is sorted
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while(l < r):
            s = numbers[l] + numbers[r]
            if (s == target):
                return [l+1, r+1]
            elif (s < target):
                l += 1
            else: # s > target
                r -= 1
        
        #throw exception
        return [l+1, r+1]