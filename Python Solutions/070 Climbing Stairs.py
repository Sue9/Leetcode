# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:09:31 2018

@author: zhaoxu

70 Climbing Stairs
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        
        
        a = 1
        b = 1
        sumN = 0
        
        
        for i in range(n-1):
            sumN = a + b
        
            b = a
            a = sumN
    
            
        return sumN
        
        """
        #fail: Time Limit Exceeded
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        """
