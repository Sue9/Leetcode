# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:00:59 2019

@author: Sue

438. Find All Anagrams in a String
"""
class Solution(object):
    def isAnagram(self, l, p):
        if (len(set(l)) != len(set(p))):
            return False
        
        for i in l:
            print("i = ", i, " p = ", p)
            if i not in p:
                return False
            else:
                p = p.replace(i, '', 1)
        return True
        
        
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        n = len(p)
        res = []
        
        for l in range(len(s) - n + 1):
            print("index l = ", l ,"s[l:l+n] = ", s[l:l+n])
            if self.isAnagram(s[l:l+n], p):
                res.append(l)
        return res
        