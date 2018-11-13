# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:51:57 2018

@author: Sue

088 Merge Sorted Array


two pointers, start from the right
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            nums1[0:len(nums2)] = nums2
        
        ind = m + n - 1
        while (ind >= 0):
            
            if (n < 1):
                break
            elif (m == 0):
                nums1[0:n] = nums2[0:n]
                break
                
            elif nums1[m-1] > nums2[n-1]:
                nums1[ind] = nums1[m-1]
                m -= 1
            else:
                nums1[ind] = nums2[n-1]
                n -= 1
            ind -= 1
            
            
            
            
            
        
        