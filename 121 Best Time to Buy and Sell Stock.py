# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:27:43 2018

@author: zhaoxu

121 Best Time to Buy and Sell Stock

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #use two pointers
        #minPrice : is the lowest price
        #maxProfit: is the current maxProfit
        maxProfit = 0
        
        
        if len(prices) == 0:
            return maxProfit
        
        minPrice = prices[0]
        
        for p in prices[1:]:
            if (p - minPrice) > maxProfit:
                maxProfit = p - minPrice
            if (p < minPrice):
                minPrice = p
        
        return maxProfit
            
        
        """
        #first try failed: time limit exceeded
        maxProfit = []
        
        for i in range(len(prices) - 1):
            tmpList = prices[i+1:]
            if(len(tmpList) != 0):
                buyP = prices[i]
                sellP = max(tmpList)
                thisMax = sellP - buyP
                if(thisMax >= 0):
                    maxProfit.append(thisMax)
        
        if len(maxProfit) == 0:
            return 0
        else:
            return max(maxProfit)
        """