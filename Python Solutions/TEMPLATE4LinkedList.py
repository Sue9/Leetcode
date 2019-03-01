# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:52:06 2019

@author: Sue

000 TEMPLATE
"""
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
        
    
