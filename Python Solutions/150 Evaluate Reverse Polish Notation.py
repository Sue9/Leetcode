# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:01:30 2019

@author: Sue

150. Evaluate Reverse Polish Notation
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        if len(tokens) == 0:
            return 0
        
        stack = []
        operators = ["+", "-", "*", "/"]
        
        for i in tokens:
            if i in operators:
                m1 = stack.pop()
                m2 = stack.pop()
                if (i == "+"):
                    n = m1 + m2
                elif (i == "-"):
                    n = m2 - m1
                elif (i == "*"):
                    n = m1 * m2
                else:# i == "/"
                    if m1 * m2 < 0:
                        n = -(int(-m2 / m1))
                    else:
                        n = int(m2 / m1)
                stack.append(n)
            else:#i is integer
                stack.append(int(i))
        res = stack.pop()
        return res
                    
            
        
        