# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:56:44 2018

@author: zhaoxu

454 4Sum II
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        
        """
        
        cnt = 0
        dic = {}
        
        for a in A:
            for b in B:
                dic[a+b] = dic.get(a+b, 0) + 1
        
        for c in C:
            for d in D:
                cnt += dic.get(-c-d, 0)
                
        return cnt
        
        
        """
        #Time Limit Exceed
        
        if len(A) == 0:
            return 0
        
        n = len(A)
        dictAB = {}
        dictCD = {}
        cnt = 0
        
        for i in range(n):
            for j in range(n):
                pos = '(' + str(i) + ',' + str(j) + ')'
                dictAB[ pos ] =   A[i] + B[j]
                dictCD[ pos ] = -(C[i] + D[j])
                
        for abValue in dictAB.values():
            cnt += list(dictCD.values()).count(abValue)
        
        return cnt
        
        """