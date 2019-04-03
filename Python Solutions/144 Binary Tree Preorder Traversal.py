# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:45:37 2019

@author: Sue

144. Binary Tree Preorder Traversal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if (root is None):
            return res
        
        stack = []
        stack.append(["go", root])
        
        while stack:
            cmd = stack.pop()
            if (cmd[0] == "print"):
                res.append(cmd[1].val)
            else:
                if (cmd[1].right):
                    stack.append(["go", cmd[1].right])
                if (cmd[1].left):
                    stack.append(["go", cmd[1].left])
                stack.append(["print", cmd[1]])
            
        
        return res