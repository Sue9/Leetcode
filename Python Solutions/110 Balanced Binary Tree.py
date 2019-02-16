# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:17:29 2019

@author: Sue

110. Balanced Binary Tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None):
            return 0
        
        return max(self.depth(root.left), self.depth(root.right)) + 1
        
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root is None):
            return True
        
        return (abs(self.depth(root.left) - self.depth(root.right)) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
