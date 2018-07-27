# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:00:11 2018

@author: zhaoxu


283 Move Zeroes
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
        nums += ([0] * n)
        
        """
        cnt = nums.count(0)
        for i in range(cnt):
            print("i = ", i, ' and nums = ',nums)
            nums.remove(0)
            print ("\t in if, nums = ", nums)
        print("before appendm nums = ", nums)
        nums += ([0]*cnt)
        print("finally, the result nums = ", nums)
        """