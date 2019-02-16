# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:36:32 2018

@author: zhaoxu

172. Factorial Trailing Zeroes
"""

class Solution(object):
    def trailingZeroes(self, n):
        if n < 5:
            return 0
        return int(n / 5) + self.trailingZeroes(n / 5)
    
    
    """
    #Maximum recursion exceed
    
    
    def fac(self, n):
        if (n == 1) or (n == 0):
            return 1
        
        return n * self.fac(n-1)
    
    def trailingZeroes(self, n):
            
        
        cnt = 0
        s = str(self.fac(n))
        for i in range(len(s) - 1):
            if s[-1-i] == '0':
                cnt += 1
            else:
                return cnt
        return cnt
        
    """
