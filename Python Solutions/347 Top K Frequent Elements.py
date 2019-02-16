# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:02:44 2018

@author: zhaoxu

347. Top K Frequent Elements
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return nums
        
        existed = []
        dict = {}
        
        for i in nums:
            if i not in existed:
                existed.append(i)
                dict[i] = nums.count(i)
        
        s = sorted(dict.items(), key=lambda d:d[1], reverse=True)[:k]
        
        return [key for key,value in s]