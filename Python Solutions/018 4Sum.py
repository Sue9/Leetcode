# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:43:41 2018

@author: zhaoxu

018 4Sum
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums) < 4:
            return []
    
        res = []
        n = len(nums)
        dicABC = {}
        
        for a in range(n - 3):
            for b in range(a+1, n - 2):
                for c in range(b+1, n - 1):
                    q = target - nums[a] - nums[b] - nums[c]
                    
                    if dicABC.get(q) != None:
                        
                        dicABC.get(q).append([nums[a], nums[b], nums[c]])
                    else:
                        dicABC[q] = [[nums[a], nums[b], nums[c]]]
                    
        
        
        for d in range(3, n):
            if dicABC.get(nums[d]) != None:
                for abc in dicABC.get(nums[d]):
                    
                    if res == []:
                        abc.append(nums[d])
                        abc.sort()
                        res = [abc]
                    else:
                        abc.append(nums[d])
                        abc.sort()
                        if abc not in res:
                            res.append(abc)
                    
        return res
        
        
        
        
        """
        if len(nums) < 4:
            return []
    
        res = []
        n = len(nums)
        nums1 = nums[:int(n/2)]
        nums2 = nums[int(n/2):]
        dicAB = {}
        
        for a in range(len(nums1)-1):
            for b in range(a+1 , len(nums1)):
                if dicAB.get(target - nums1[a] - nums1[b]) != None:
                    dicAB[ target - nums1[a] - nums1[b] ] = dicAB.get(target - nums1[a] - nums1[b]).append([nums1[a], nums1[b]])
                else:
                    dicAB[ target - nums1[a] - nums1[b] ] = [[nums1[a], nums1[b]]]
        print(dicAB)
        for c in range(len(nums2)-1):
            for d in range(c+1, len(nums2)):
                if dicAB.get(nums2[c]+nums2[d]) != None:
                    cd = [nums2[c], nums2[d]]
                    print('cd = ', cd)
                    print('dicAB = ', dicAB.get(nums2[c]+nums2[d]))
                    for ab in dicAB.get(nums2[c]+nums2[d]):
                        res.append(ab+cd)
        return res
        """
                    
                
        