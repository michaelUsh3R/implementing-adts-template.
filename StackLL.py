# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         FIXME
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.add(item)

    def peek(self):
        # FIXME
        return

    def pop(self):
        # FIXME
        return

    def push(self, data=None):
        # FIXME
        return

    def print(self):
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        # FIXME
        return

    def clear(self):
        # FIXME
        return

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

