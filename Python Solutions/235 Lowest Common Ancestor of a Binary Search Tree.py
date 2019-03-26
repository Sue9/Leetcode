# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:03:20 2019

@author: Sue

235. Lowest Common Ancestor of a Binary Search Tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isDescendant(self, root, p):
        if (root is None):
            return False
        
        if (root == p):
            return True
        
        return self.isDescendant(root.left, p) or self.isDescendant(root.right, p)
        
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if (root is None):
            return None
        
        if (p is None):
            return q
        
        if (q is None):
            return p
        
        if (p is None) and (q is None):
            return None
        
        if (p.val < root.val) and (q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val) and (q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
    
    """
    
        
        if (p == root) or (q == root):
            return root
        
        if (self.isDescendant(root.left, p) and self.isDescendant(root.right, q)) or (self.isDescendant(root.right, p) and self.isDescendant(root.left, q)):
            return root
        
        if (self.isDescendant(root.left, p)):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
            
        """
    """
        
