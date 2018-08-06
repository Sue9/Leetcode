# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:52:16 2018

@author: zhaoxu

242. Valid Anagram

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        lt = list(t)
        ls = list(s)
        
        for i in lt:
            if i not in ls:
                return False
            else:
                ls.remove(i)
        
        return (ls == [])
