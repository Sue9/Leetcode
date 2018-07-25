# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:02:23 2018

@author: zhaoxu

773 Jewels and Stones
"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        s = 0
        for j in J:
            s += S.count(j)
        
        return s

