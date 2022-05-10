# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        self.top = -1
        self.max = 100
        self.list = [0 for i in range(self.max)]

        if list is not None:
            for item in list:
                self.add(item)

    def peek(self): # peek function for the queue
        return self.list[self.top]

    def pop(self): # Removes the head node and makes the preceding one the new head
        if (self.is_empty()):
            return None
        item = self.list[self.top]
        self.top = self.top - 1
        self.list.pop()
        return item

    def push(self, data=None): # pushes the items to the queue
        self.top = self.top + 1
        self.list[self.top] = data

    def print(self): #prints the list
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.top == -1

    def clear(self):  # clears the list
        self.front = None
        self.tail = None

def main():
    s = StackLL()
    le = []
    la = []
    for i in range(20, 201, 10):
        s.push(i)
        le.insert(0, i)
    while not s.is_empty():
        la.append(s.pop())
    print(le==la)

# Don't run main on import
if __name__ == "__main__":
    main()
