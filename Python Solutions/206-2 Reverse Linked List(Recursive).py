# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:30:41 2018

@author: Sue

206 Reverse Linked List


https://blog.csdn.net/huhehaotechangsha/article/details/80467450
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseHelper(self, head, new):
        if not head:
            return new
        
        
        recur = head.next
        head.next = new
        return self.reverseHelper(recur, head)
        
        
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #recursion
        new = None
        return self.reverseHelper(head, new)
        
        
        
        """
        #iteration shorter version, faster than 100%
        new = None
        p = None
        
        while head:
            p = head
            #Caution: order of the following two 
            head = head.next
            p.next = new
            
            new = p
            
        return new
        """  
        
        
        
        """
        
        #Iteration
        if not head:
            return head
        
        new = ListNode(head.val)
        tail = head.next
        
        while tail:
            node = ListNode(tail.val)
            node.next = new
            new = node
            
            tail = tail.next
            
        return new
        """
        
        
        
        
