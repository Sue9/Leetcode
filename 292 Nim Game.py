# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:11:18 2018

@author: zhaoxu


292. Nim Game
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return not(n % 4 == 0)

