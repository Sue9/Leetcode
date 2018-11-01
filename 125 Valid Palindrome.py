# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:34:49 2018

@author: zhaoxu


125 Valid Palindrome
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
#        print('s = ' , s)
        t = ''
        
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                t += i
#        print('t = ', t)
        
        return t == t[::-1]
        
