# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:00:35 2019

@author: Sue

142. Linked List Cycle II
"""
#use set to store each position
#return None if there isn't cycle
#return the cycle head if there is cycle

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast.next and fast.next.next:
            if fast == slow:
                #cycle
                slow2 = head
                while slow2 is not slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow2
            else:
                fast = fast.next.next
                slow = slow.next
            
        #no cycle
        return fast.next
        


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    
        