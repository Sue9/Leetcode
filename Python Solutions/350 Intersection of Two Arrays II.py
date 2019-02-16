# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:08:06 2018

@author: Sue

350 Intersection of Two Arrays II


1.choose longer nums, convert it into hashmap
2.do for-loop on shoter nums, append elements on the result
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        dic1 = {}
        
        for i in nums1:
            dic1[i] = dic1.get(i, 0) + 1
        
        for j in nums2:
            if (dic1.get(j) != None) and (dic1.get(j) > 0):
                res.append(j)
                dic1[j] -= 1
        
        return res
        