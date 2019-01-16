# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:34:57 2019

@author: Sue

572. Subtree of Another Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution(object):
    def isSameTree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if (s is None):
            return (t is None)
        
        if (t is None):
            return False
        
        if (s.val != t.val):
            return False
        
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        
    
    
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if (s is None):
            return (t is None)
        
        # s is not None, t is None
        if (t is None):
            return False
        
        # s is not None && t is not None
        if (s.val == t.val):
            return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        
        
        