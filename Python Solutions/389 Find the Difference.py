# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:23:41 2018

@author: zhaoxu

389. Find the Difference
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if i not in s:
                return i
            s = s.replace(i, "", 1)
        