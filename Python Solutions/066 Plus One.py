# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:28:57 2018

@author: zhaoxu

66. Plus One
"""

class Solution(object):
    
    
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if (len(digits) == 1) and (digits[0] == 9):
            return [1,0]
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            return self.plusOne(digits[:-1]) + [digits[-1]]