# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:49:53 2019

@author: Sue

345. Reverse Vowels of a String

"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        r = len(s) - 1
               
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
        ls = list(s)
        
        while (l < r):
            if (ls[l] in vowel) and (ls[r] in vowel):
                ls[l], ls[r] = ls[r], ls[l]
                l += 1
                r -= 1
            elif (ls[l] in vowel):
                r -= 1
            elif (ls[r] in vowel):
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(ls)
        