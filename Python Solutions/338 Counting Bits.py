# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:11:52 2018

@author: Sue


338 Counting Bits
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num == 0:
            return [0]
        
        res = [0,1]
#        power2 = 1
        num2 = 2
        
        for i in range(2, num+1):
            if i == num2:
                res.append(1)
#                power2 += 1
                num2 = 2 * num2
            else:
                residue = i - num2
                res.append(1 + res[residue])
            
        return res
            