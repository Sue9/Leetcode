# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:30:22 2018

@author: zhaoxu


7. Reverse Integer
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            new_num = int(str(x)[::-1])
        else:
            new_num = -int(str(x)[1:][::-1])
        
        if (new_num >= pow(-2, 31)) and (new_num <= pow(2,31) - 1):
            return new_num
        else:
            return 0