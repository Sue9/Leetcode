# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:45:28 2019

@author: Sue

563 Binary Tree Tilt (optimised version)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.tilt = 0
        
        def sumNodes(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if (root is None):
                return 0
            
            lsum = sumNodes(root.left)
            rsum = sumNodes(root.right)
            
            self.tilt += abs(lsum - rsum)
            
            return (lsum + rsum + root.val)
        
        sumNodes(root)
        return self.tilt
            
            