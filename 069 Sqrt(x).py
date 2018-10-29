# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:22:11 2018

@author: zhaoxu


069 Sqrt(x)
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        while(r * r <= x):
            r += 1
        
        return r - 1

