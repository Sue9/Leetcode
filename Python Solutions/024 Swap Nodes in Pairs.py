# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:04:25 2019

@author: Sue

024. Swap Nodes in Pairs
"""
#import TEMPLATE4LinkedList as template

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head is None) or (head.next is None):
            return head
        
        dummy = prev = ListNode(0)
        dummy.next = head
        cur = head
        
        while(cur and cur.next):
            even = cur.next
            cur.next = cur.next.next
            even.next = cur
            prev.next = even
            #update
            cur = cur.next
            prev = prev.next.next
            
        return dummy.next
        
    
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


