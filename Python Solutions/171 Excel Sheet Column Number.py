# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:39:09 2018

@author: zhaoxu


171 Excel Sheet Column Number
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0
        
        for r in range(l):
            i += (ord(s[r]) - 64) * (26 ** (l - 1 - r))    
        
        return i