# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 5: Queue-Array
#
# NAME:         FIXME
# ASSIGNMENT:   Technical HW: Implementing ADTs

class QueueArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.front = -1
        self.tail = -1

    def get_front(self):
        # FIXME
        return

    def get_tail(self):
        # FIXME
        return

    def deq(self):
        # FIXME
        return

    def enq(self, data=None):
        # FIXME
        return


    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        # FIXME
        return

    def clear(self):
        # FIXME
        return

    def is_full(self):
        l = self.size()
        return l >= len(self.array)

    def size(self):
        if self.front == -1:
            return 0
        l = self.tail - self.front + 1
        if self.tail < self.front:
            l = len(self.array) - self.front + self.tail + 1
        return l


def main():
    s = QueueArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 4):
        s.enq(i)
        #print("Size:", s.size())
        #s.print()
    s.print()
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    s.print()
    for i in range(5, 11):
        s.enq(i)
        #print("Size:", s.size())
        #s.print()
    print("Front:", s.get_front())
    print("Tail: ", s.get_tail())
    print("Deq:  ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())
    print("Size:", s.size())


# Don't run main on import
if __name__ == "__main__":
    main()

