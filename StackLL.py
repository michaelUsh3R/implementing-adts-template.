# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.add(item)

    def peek(self): # peek function for the queue
        if self.isempty():
            return None
        else:
            return self.head.data

    def pop(self): # Removes the head node and makes the preceding one the new head
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def push(self, data=None): # pushes the items to the queue
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def print(self): #prints the list
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self): # checks if the list is empty
        if self.head == None:
            return True
        else:
            return False

    def clear(self): # clears the list
        self.front = None
        self.tail = None

def main():
    s = StackLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.push(i)
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    while not s.is_empty():
        print(s.pop())

# Don't run main on import
if __name__ == "__main__":
    main()

