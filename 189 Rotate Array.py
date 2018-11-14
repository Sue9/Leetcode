# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:31:41 2018

@author: Sue


189 Rotate Array

At least three ways
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        left = nums[:n-k]
        right = nums[n-k:]
        nums[:] = right + left
        
        