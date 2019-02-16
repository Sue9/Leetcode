# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:53:01 2018

@author: zhaoxu

191 Number of 1 Bits
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n)[2:].count('1')