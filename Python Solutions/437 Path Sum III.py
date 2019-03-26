# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:45:06 2019

@author: Sue

437. Path Sum III
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def containNode(self, root, sum):
        """
        calcuate how many path is valid from root, that sums up to the given value
        """
        if (root is None):
            return 0
        
        res = 0
        if (root.val == sum):
            res += 1
        
        res += self.containNode(root.left, sum - root.val)
        res += self.containNode(root.right, sum - root.val)
        
        return res
    
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if (root is None):
            return 0
        
        res = self.containNode(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        
        return res