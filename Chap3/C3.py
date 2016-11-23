#Tower of hanoi attempt

import sys

class node:

    def __init__(self,cargo=None, nextNode=None):
        self.cargo = cargo
        self.nextNode = nextNode

class Stack:

    def __init__(self):
        self.head = None
        self.second_2_last = None


    def push(self,value):
        if self.head==None:
            newNode = node()
            self.head = newNode
            newNode.cargo = value
            return

        temp = self.head
        while temp.nextNode != None:
            temp = temp.nextNode
        newNode = node()
        temp.nextNode = newNode
        newNode.cargo = value
        self.second_2_last = temp

    #@staticmethod
    def pop(self):
        temp = self.second_2_last
        del (temp)

        print self.second_2_last.cargo

    def __str__(self):
        temp = self.head
        l = []
        while temp !=None:
            l.append(str(temp.cargo))
            l.append('\n')
            temp = temp.nextNode
        return ''.join(l)

class MyQueue:

    def __init__(self):
        self.S1 = Stack()
        self.S2 = Stack()


    def remove(self):
        if not self.S2:
            while self.S1 :
                self.S2.push(self.S1)
        self.S2.pop()

    def add_element(self,value):
        self.S1.push(value)

def main():
    S1 = Stack()
    S1.push(2)
    S1.push(3)
    S1.push(5)
    S1.push(10)

    #print S1
    S1.pop()
    #print S1


if __name__ == '__main__':
    main()