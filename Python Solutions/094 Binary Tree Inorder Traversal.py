# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:34:40 2018

@author: zhaoxu


94 Binary Tree Inorder Traversal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        if (not root.left) and (not root.right):
            return [root.val]
        elif (not root.left):
            return [root.val] + self.inorderTraversal(root.right)
        elif (not root.right):
            return self.inorderTraversal(root.left) + [root.val]
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
            
        
        