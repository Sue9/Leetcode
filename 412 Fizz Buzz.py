# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:12:10 2018

@author: zhaoxu

412 Fizz Buzz
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ls = []
        
        for i in range(1,n+1):
            s = ""
            if (i % 3) == 0:
                s += "Fizz"
            if (i % 5) == 0:
                s += "Buzz"
            if len(s) == 0:
                s = str(i)
            ls.append(s)
        return ls
            