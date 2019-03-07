# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:01:43 2019

@author: Sue

343. Integer Break
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n <= 2):
            return 1
        
        m = [0] * (n+1)
        m[0] = m[1] = m[2] = 1
        
        for i in range(3, n+1):
            for j in range(1, i):
                temp = max(j * (i - j), j * m[i-j])
                m[i] = max(m[i], temp)
                
        return m[n]