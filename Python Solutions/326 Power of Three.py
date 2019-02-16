# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:42:20 2018

@author: zhaoxu

326. Power of Three
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 0:
            return False
        if n == 1:
            return True
        
        while (n > 3):
            n = n / 3.0
        return (n - 3.0) == 0