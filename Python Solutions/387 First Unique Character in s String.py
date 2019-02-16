# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:14:13 2018

@author: zhaoxu

387 First Unique Character in s String
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #this is accepted, which means functin 'in' is faster than function 'count'
        #but the overall speed is still low, which could only beat 8% other python solution
        for i in range(len(s)):
            if (s[i] not in s[0:i]) and (s[i] not in s[i+1:]) :
                return i
            
        return -1
        
        
        """
        #fail: time limit exceeded
        
        if len(s) == 0 :
            return -1
        
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
            
        return -1
        """