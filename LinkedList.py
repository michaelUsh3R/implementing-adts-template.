# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         FIXME
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    def get_head(self):
        # FIXME
        return

    def add(self, data):
        # FIXME
        return

    def search(self, data):
        # FIXME
        return

    def delete(self, data):
        # FIXME
        return

    def print(self):
        n = self.head
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
    l = list(range(1, 5))
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    ll.print()

# Don't run main on import
if __name__ == "__main__":
    main()

