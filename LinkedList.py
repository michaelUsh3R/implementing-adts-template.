# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    def get_head(self):
        if self.head is not None:  # check whether the head is none
            return self.head.get_data()
        else:
            return None

    def add(self, data): # make next node as head, and move head to point to node
        node = Node(data)
        node.next = self.head
        self.head = node
        return

    def search(self, data): # make current node the head, traverse till last node, if node with data found then return true
        curr = self.head  # make curr node to head

        while curr != None:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def delete(self, data): # deletes the selected node
        curr = self.head
        if curr != None and curr.data == data:
            self.head = curr.next
            curr = None
            return data
        while curr != None:
            if curr.data == data:
                prev.next = curr.next
                curr = None
                return data
            prev = curr
            curr = curr.next
        return None

    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self): # checks if empty by seeing if the head is none
        if self.head is not None:
            return False
        else:
            return True

    def clear(self): # deletes the list
        temp = self.head
        if temp is None:
            print("\n Not possible to delete empty list")
        while temp:
            self.head = temp.get_next()
            temp = None
            temp = self.head

def main():
    l = []
    l.reverse()
    ll = LinkedList(l)
    le = []
    la = []
    for i in range(20, 201, 10):
        ll.add(i)
        le.append(i)
    for i in range(20, 201, 10):
        la.append(ll.delete(i))
    print("Search 4: ",le==la)

if __name__ == "__main__":
    main()
