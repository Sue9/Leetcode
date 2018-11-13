# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:59:22 2018

@author: Sue


13 Roman to Integer
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        res = 0
        
        while s:
            if len(s) >= 2:
                if dic.get(s[0:2]) == None:
                    res += dic.get(s[0])
                    s = s[1:]
                else:
                    res += dic.get(s[0:2])
                    s = s[2:]
            else:
                res += dic.get(s[0])
                s = s[1:]
        
        return res