# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:23:09 2018

@author: zhaoxu



"""

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        bstr = bin(N)[2:]
        numOne = bstr.count('1')
        if( numOne ) <= 1:
            return 0
        
#        left = bstr.index('1')
        left = 0
        gaps = []
        for i in range(1, len(bstr) - bstr[::-1].index('1') , 1):
            if bstr[i] == '1':
                right = i
                gaps.append(right - left)
                left = i
                
        return max(gaps)
        