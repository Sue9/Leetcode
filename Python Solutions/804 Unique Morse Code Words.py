# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:06:40 2018

@author: zhaoxu

804. Unique Morse Code Words
"""

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        trans = []
        
        for w in words:
            s = ""
            for n in w:
                s += morse[ ord(n)- 97 ]
            
            if s not in trans:
                trans.append(s)
        
        return len(trans)
        

