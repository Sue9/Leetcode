# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:08:24 2019

@author: Sue

450. Delete Node in a BST
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSuccessor(self, root):
        """
        find the rightmost leaf of current root
        :return: (successor value, new root)
        :rtype: (int, TreeNode)
        """
        if (root is None):
            return (None, None)
        
        if (root.left is None) and (root.right is None):
            return (root.val, None)
        
        if (root.right is None): # root.left is not None
            return (root.val, root.left)
        
        (s, newRight) = self.findSuccessor(root.right)
        root.right = newRight
        
        return (s, root)
            
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if (root is None):
            return None
        
        if (key < root.val):
            root.left = self.deleteNode(root.left, key)
            return root
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
            return root
        elif (key == root.val):
            #if (root.left is None) and (root.right is None):
            #    return None
            if (root.left is None):
                return root.right
            if (root.right is None):
                return root.left
            #successor is the leftmost of the right child, or the rightmost of the left child
            (s, newLeft) = self.findSuccessor(root.left)
            newRoot = TreeNode(s)
            newRoot.left = newLeft
            newRoot.right = root.right
            return newRoot           
            
            
        else: #key does not exist
            return root
            
        