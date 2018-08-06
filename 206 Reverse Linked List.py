# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:30:41 2018

@author: zhaoxu

206 Reverse Linked List
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #Recursive
        if not head or not head.next:
            
            return head
        
        
        
        ln = self.reverseList( head.next )
        
        ln.next = ListNode( head.val )
        
        return ln

#        if not head:
#            return head
        
        
