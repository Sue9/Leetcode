# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:14:32 2019

@author: Sue

107. Binary Tree Level Order Traversal II
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue
class Solution:
    def levelOrderBottom(self, root: TreeNode): # -> List[List[int]]:
        if (root is None):
            return []
        
        q = Queue()
        res = []
        #pair: (level, node)
        q.put((0, root))
        
        while(not q.empty()):
            top = q.get()
            node = top[1]
            level = top[0]
            
            if(level >= len(res)):
                res.append([node.val])
            else:
                res[level].append(node.val)
            
            if( node.left ):
                q.put((level+1, node.left))
            if( node.right ):
                q.put((level+1, node.right))
        
        rev_res = []
        for i in res:
            rev_res = [i] + rev_res
        
        return rev_res