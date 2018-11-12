# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:35:49 2018

@author: Sue


108 Convert Sorted Array to Binary Search Tree

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid  = (len(nums) // 2)
        left  = nums[0:mid]
        right = nums[mid+1:]
        
        t = TreeNode(nums[mid])
        t.left  = self.sortedArrayToBST(left)
        t.right = self.sortedArrayToBST(right)
        
        return t