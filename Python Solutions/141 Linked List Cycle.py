# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:04:19 2019

@author: Sue

141. Linked List Cycle
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        Algorithm:
            use two pointers, p1 and p2
            p1 goes one step each time, while p2 goes two
            return True if p1 and p2 encounter
            else False (or False if p2 goes to the end of the list)
        """
        if (head is None):
            return False
        
        fast = head
        slow = head
        
        while (fast and fast.next):
            
            slow = slow.next
            fast = fast.next.next
            if (fast == slow):
                return True
        return False