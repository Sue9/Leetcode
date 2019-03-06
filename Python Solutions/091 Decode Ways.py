# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:04:01 2019

@author: Sue

091. Decode Ways
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        if (n == 0):
            return 0
        
        if (s[0] == "0"):
            return 0
        
        #s[0] != "0"
        if (n == 1):
            return 1
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        
        for i in range(1, n+1):
            #print("i = ", i)
            dp1 = dp2 = 0
            if (s[i-1] != "0"):
                dp1 = dp[i-1]
            if (i - 2 >= 0) and (int(s[i-2:i]) >= 10) and (int(s[i-2:i]) <= 26):
                dp2 = dp[i-2]
            dp[i] = dp1 + dp2
            #print("dp = ", dp)
        return dp[n]
        
        """
        #Recursive: Time Limit Exceed
        if (len(s) == 0) or (s[0] == "0"):
            return 0        
        
        if (len(s) == 1):
            return 1
        
        if (len(s) == 2):
            if (int(s) <= 26) and (s[1] != "0"):
                return 2
            elif (int(s) > 26) and (s[1] == "0"):
                return 0
            else:
                return 1
        
        #len(s) > 1
        
        if(int(s[0:2]) <= 26):
            n2 = self.numDecodings(s[2:])
        else:
            n2 = 0
        n1 = self.numDecodings(s[1:])
        return n1+n2

        """
        