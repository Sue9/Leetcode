# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:21:34 2018

@author: Sue

020 Valid Parentheses

Algorithm:
    two criteria:
        1) if right > left, fail
        2) when adding right parenthesis, if other pairs' left != right
"""

class Solution(object):
    def leftPair(self, s):
        """
        :type s: char
        :rtype: char
        """
        
        if s == ')':
            return '('
        if s == ']':
            return '['
        if s == '}':
            return '{'
    
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
#        dic = {'(': 0, ')':0, '[': 0, ']': 0, '{': 0, '}': 0 }
        lastOpen = ''
        left  = ['{', '(', '[']
#        right = ['}', ')', ']']
    
        for i in s:
            if i in left:
                lastOpen += i
            else:
                if len(lastOpen) == 0:
                    return False
                elif lastOpen[-1] != self.leftPair(i):
                    return False
                else:
                    lastOpen = lastOpen[:-1]
        
        return len(lastOpen) == 0
                