# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:19:49 2019

@author: Sue

445. Add Two Numbers II
"""
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 is None):
            return l2
        if(l2 is None):
            return l1
        
        stack1 = list()
        stack2 = list()
        
        while(l1):
            stack1.append(l1.val)
            l1 = l1.next
        while(l2):
            stack2.append(l2.val)
            l2 = l2.next
        
        if(len(stack1) <= len(stack2)):
            short = stack1
            long = stack2
        else:
            short = stack2
            long = stack1
        
        carry = 0
        cur = None
        while(short):
            s = short.pop() + long.pop() + carry
            carry = s // 10
            s = s % 10
            node = ListNode(s)
            node.next = cur
            cur = node
            
            
        while(long):
            s = long.pop() + carry
            carry = s // 10
            s = s % 10
            node = ListNode(s)
            node.next = cur
            cur = node
            
        if (carry):
            node = ListNode(carry)
            node.next = cur
            cur = node
        return cur
            
            
            
        

def printListNode(head):
    s = ""
    while(head):
        s += str(head.val) + " -> "
        head = head.next
    s += "NULL"
    return s
        
def createListNode(arr):
    if(arr == []):
        return ListNode(None)
        
    res = ListNode(arr[0])
    head = res
    for i in range(1, len(arr)):
        head.next = ListNode(arr[i])
        head = head.next
    return res


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None        