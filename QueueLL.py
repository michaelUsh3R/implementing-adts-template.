# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Queue-LL
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class QueueLL(object):
    def __init__(self, list=None):
        self.front = None
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)

    def get_front(self): # returns data at the front of the queue
        if self.front is not None:
            return self.front.get_data()
        return None

    def get_tail(self): # returns data at the tail of the queue
        if self.tail is not None:
            return self.tail.get_data()
        return None

    def deq(self): # returns data at the front and removes the front node and updates front
        if self.is_empty(): return None
        front_node = self.front
        self.front = self.front.get_next()
        return front_node.get_data()

    def enq(self, data=None): # adds item to the back of the queue
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self): # returns true if queue is empty
        return self.front is None

    def clear(self): # clears all items in the queue
        self.front = None
        self.tail = None

def main():
    s = QueueLL()
    le = []
    la = []
    for i in range(20, 201, 10):
        s.enq(i)
        le.append(i)
    while not s.is_empty():
        la.append(s.deq())
    print(le == la)

# Don't run main on import
if __name__ == "__main__":
    main()
