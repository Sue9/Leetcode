# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:06:39 2018

@author: zhaoxu

371 Sum of Two Integers
"""

class Solution(object):
    
    
        
        
    
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        
        if a > b:
            return self.getOrderSum(b, a)
        else:
            return self.getOrderSum(a, b)
        
        
    def getOrderSum(self, short, long):
        """
        :type short: int
        :type long : int
        :rtype: int
        """
        
        bs = bin(short)[2:][::-1]
        bl = bin(long )[2:][::-1]
        
        lshort = len(bs)
        llong  = len(bl)
#        ldiff  = llong - lshort + 1
        carry = 0
        
        revStr = ''
        
        for i in range(lshort):
#            print("i = ",i)
            s = int(bs[i]) ^ int(bl[i]) ^ carry
#            print("s = ",s)
            revStr += str(s)
#            print("revStr",revStr)
                   
            if [int(bs[i]), int(bl[i]), carry].count(1) > 1:
                carry = 1
            else:
                carry = 0
#            print(carry)
        
        
            

        for i in range(lshort, llong, 1):
            s = int(bl[i]) ^ carry
#            print("i = ",i)
            revStr += str(s)
#            print("s = ",s)
            if [int(bl[i]), carry].count(1) > 1:
                carry = 1
            else:
                carry = 0
#            print(carry)
        
        if carry == 1:
            revStr += '1'
            
        
        return int(revStr[::-1],2)
            
        
        
        
            
            
            