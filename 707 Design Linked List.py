# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:18:15 2019

@author: Sue

707. Design Linked List
"""


class MyLinkedList(object):
    class MyNode:
        def __init__(self, val, nextNode):
            self.val = val
            self.next = nextNode
            

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = None
        self.size = 0

        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if (index < 0) or (index + 1 > self.size):
            return -1
    
        p = self.list
        while (index):
            p = p.next
            index -= 1
        
        return p.val
        
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        
        node = self.MyNode(val, self.list)
        self.list = node
        self.size += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        
        if(self.size == 0):
            self.list = self.MyNode(val, self.list)
            
        #self.size > 0
        else:
            node = self.MyNode(val, None)
            c = self.size - 1
            p = self.list
            while (c):
                p = p.next
                c -= 1
                p.next = node
#            self.list = p
        self.size += 1
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if (index < 0) or (index > self.size):
            return
        elif (index == self.size):
            self.addAtTail(val)
            
        # (index >= 0) and (index < self.size)
        else:        
            prev = self.MyNode(-1, self.list)
            while (index):
                prev = prev.next
                index -= 1
            q = self.MyNode(val, prev.next)
            prev.next = q
            self.size += 1
                
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if(self.size == 0):
            return
        
        if (index > self.size - 1) or (index < 0):
            return
        #(index <= self.size - 1) and (index >= 0)
        #(self.size != 0)
        else:
            return
            
            
        
        
        
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)