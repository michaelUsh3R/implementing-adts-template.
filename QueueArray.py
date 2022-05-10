# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 5: Queue-Array
#
# NAME:         Michael Usher
# ASSIGNMENT:   Technical HW: Implementing ADTs

class QueueArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.front = -1
        self.tail = -1

    def get_front(self): #gets the front
        if self.is_empty():
            return None
        return self.array[self.front]

    def get_tail(self): # gets the tail
        if self.is_empty():
            return None
        return self.array[self.tail]

    def deq(self): # deques the array
        if self.is_empty():
            return None
        front = self.array[self.front]
        size = self.size()
        if size == 1:
            self.front = -1
            self.tail = -1
        else:
            self.front = (self.front + 1) % len(self.array)
        return front

    def enq(self, data=None): # enques the array
        if self.is_full():
            big_array = [0 for i in range(len(self.array) * 2)]
            for i in range(self.front, self.front + self.size(), 1):
                big_array[i % len(big_array)] = self.array[i % len(self.array)]
            self.front = 0
            self.tail = self.size() - 1
            self.array = big_array
        if self.is_empty():
            self.front = 0
        self.tail = (self.tail + 1) % len(self.array)
        self.array[self.tail] = data


    def print(self): #prints
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

    def is_empty(self): # check if it is empty
        return self.front == -1

    def clear(self): # clears the array
        self.front = -1
        self.tail = -1

    def is_full(self): # check if it is full
        l = self.size()
        return l >= len(self.array)

    def size(self): # returns the size of array
        if self.front == -1:
            return 0
        l = self.tail - self.front + 1
        if self.tail < self.front:
            l = len(self.array) - self.front + self.tail + 1
        return l

def main():
    s = QueueArray()
    le = []
    la = []
    for i in range(20, 201, 10):
        s.enq(i)
        le.append(i)
    while not s.is_empty():
        la.append(s.deq())
    print(le==la)

if __name__ == "__main__":
    main()
