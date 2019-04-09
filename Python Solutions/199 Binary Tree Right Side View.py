# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:27:48 2019

@author: Sue

199. Binary Tree Right Side View
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue
class Solution:
    def rightSideView(self, root: TreeNode): # -> List[int]:
        
        if(root is None):
            return []
            
        bfs = []
        q = Queue()
        q.put((0, root))
        while (not q.empty()):
            top = q.get()
            node = top[1]
            level= top[0]
            if (level >= len(bfs)):
                bfs.append(node.val)
            else:
                bfs[level] = node.val
            
            if(node.left):
                q.put((level+1, node.left))
            if(node.right):
                q.put((level+1, node.right))
        return bfs