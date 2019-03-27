# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:35:38 2019

@author: Sue

236. Lowest Common Ancestor of a Binary Tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    def isDescendant(self, root, p):
        if (root is None):
            return False
        
        if (p == root):
            return True
        
        return self.isDescendant(root.left, p) or self.isDescendant(root.right, p)
    """ 
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if (root is None) or (p == root) or (q == root):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if (left and right):
            return root
        
        if (left):
            return left
        else:
            return right
        
        