# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:13:26 2019

@author: Sue

215. Kth Largest Element in an Array
"""
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
        