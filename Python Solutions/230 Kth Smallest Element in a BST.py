# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:55:25 2019

@author: Sue

230. Kth Smallest Element in a BST
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inOrder(self, root):
        """
        :type root: TreeNode
        :type k: int
        :type sz: int
        :rtype: List
        """
        if(root is None):
            return []
        
        l1 = self.inOrder(root.left)
        l2 = self.inOrder(root.right)
        
        return l1 + [root.val] + l2
        
        
        
        
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = self.inOrder(root)
        return l[k - 1]
        