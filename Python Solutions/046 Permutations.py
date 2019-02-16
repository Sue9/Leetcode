# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:01:26 2018

@author: zhaoxu

46. Permutations
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if (len(nums) <= 1):
            return [nums]
#        print("test1")
        
        ll = []
        
        for i in nums:
#            print('i = ', i)
            tp = list(nums)
            tp.remove(i)
#            print('subNums = ', tp)
            subPermute= self.permute(tp) 
#            print('subPer = ', subPermute)
            ltp = map(lambda x:[i]+x, subPermute)
            
            ll.extend(list( ltp ))
#            print('ll = ',ll)
        
        return ll
            
            

