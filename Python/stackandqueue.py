import hashlib
class Inode():
    def __init__(self, value):
        self.value = value
        self.previous = None

head = None
headActive = None
class Queue():

    def AppendInode(self, value):
        others = Inode(value)
        global head, headActive
        if head == None:
            head = others
            headActive = others
        else:
            headActive.previous = others
            headActive = others

    def pop(self):
        global head
        head = head.previous

    def PrintQueue(self):
        global head
        tmp = head
        while (tmp != None):
            print(tmp.value)
            tmp = tmp.previous


class Stack():
    head = None
    def add(self, value):
        others = Inode(value)
        if self.head == None:
            self.head = others
        else:
            others.previous = self.head
            self.head = others
    
    def pop(self):
        self.head = self.head.previous
    
    def printStack(self):
        tmp = self.head
        while (tmp != None):
            print(tmp.value)
            tmp = tmp.previous

