# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:21:36 2019

@author: Sue

098. Validate Binary Search Tree
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
        :rtype: List
        """
        l = []
        if (root is None):
            return []
        
        l += self.inOrder(root.left)
        l.append(root.val)
        l += self.inOrder(root.right)
        
        return l
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = self.inOrder(root)
        
        for i in range(len(l)-1):
            if l[i] >= l[i+1]:
                return False
        
        return True
        