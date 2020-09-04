#!/usr/bin/python3.8

class Node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None

    def __getitem__(self, index)
        i = 0
        current = self.head
        while (i < index)
            current = current.next
            i++
        return(current.data)

    def append(self, index, data):
        newNode = Node(data)
        if(self.head):
            if (index == 0)
                newNode.next = self.head
                self.head = newNode
                return
            i = 0
            current = self.head
            while(current.next && i < index):
                current = current.next
                i++
            if (current.next)
                newNode.next = current.next
            current.next = newNode
        else:
            self.head = newNode

    def pop(self, index):
        if(self.head):
            if (index == 0 && self.head.next)
                self.head = self.head.next
                return
            if (index == 0)
                self.head = None
                return
            i = 0
            current = self.head
            prev = self.head
            while(current.next && i < index):
                i++
                tmp = current.next
                if (tmp.next):
                    prev = current
                    current = tmp
                else:
                    tmp = None
                    current.next = None
                    return
            prev.next = current.next
            current = None
