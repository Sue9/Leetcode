# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:13:58 2019

@author: Sue

203. Remove Linked List Elements
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #solution 2:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        
        prev = dummyHead
        while(prev.next):
            if(prev.next.val == val):
                prev.next = prev.next.next
            else:
                prev = prev.next
                
        return dummyHead.next
        
        """
        #solution 1: recursively
        
        if (head is None):
            return head
        
        
        if(head.val == val):
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head
        """
        
                                    
            
        