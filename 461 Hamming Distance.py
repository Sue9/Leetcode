# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:33:32 2018

@author: zhaoxu

461. Hamming Distance
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        sx = bin(x)[2:]
        sy = bin(y)[2:]
        
        lx = len(sx)
        ly = len(sy)
        
        if lx > ly:
            sy = '0' * (lx - ly) + sy
        elif ly > lx:
            sx = '0' * (ly - lx) + sx
        
        cnt = 0
        for i in range(len(sx)):
            if sx[i] != sy[i]:
                cnt += 1
        
        return cnt
        