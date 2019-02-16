# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:36:42 2018

@author: Sue

349 Intersection of Two Arrays

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        dic1 = dict(zip(nums1, [0]*(len(nums1))))
        
        for i in set(nums2):
            if dic1.get(i) != None:
                res.append(i)
                
        return res
        
        