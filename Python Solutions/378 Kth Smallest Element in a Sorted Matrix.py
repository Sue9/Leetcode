# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:28:18 2019

@author: Sue

378. Kth Smallest Element in a Sorted Matrix
"""
import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #n = len(matrix)
        #col = int(n / k)
        #row = n % k
        
        l = matrix[0]
        for m in (matrix[1:]):
            l += m
        
        print(l)
        #heap = heapq.heapify(l)
        m = heapq.nsmallest(k, l)
        print("m = ", m)
        return max(m)