# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:19:45 2018

@author: zhaoxu

38 Count and Say
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        lastStr = self.countAndSay(n - 1)
        
        if (len(lastStr) == 1):
            return "1"+lastStr
        else:
            retStr = ''
            cnt = 1
            for i in range(len(lastStr) - 1):
                
                if lastStr[i] == lastStr[i+1]:
                    cnt += 1
                    
                else:
                    
                    retStr = retStr + str(cnt) + lastStr[i]
                    
                    cnt = 1
            
            retStr = retStr +str(cnt) + lastStr[-1]
            return retStr
        

        
