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

    # Function to insert an element
    # at the rear of the queue
    def queueEnqueue(self, data):
        # Check queue is full or not
        if (self.capacity == self.rear):
            print("\nQueue is full")
        # Insert element at the rear
        else:
            self.queue.append(data)
            self.rear += 1

    # Function to delete an element
    # from the front of the queue
    def queueDequeue(self):
        # If queue is empty
        if (self.front == self.rear):
            print("Queue is empty")
        # Pop the front element from list
        else:
            x = self.queue.pop(0)
            self.rear -= 1

    # Function to print queue elements
    def queueDisplay(self):
        if (self.front == self.rear):
            print("\nQueue is Empty")
        # Traverse front to rear to
        # print elements
        for i in self.queue:
            print(i, "<--", end='')

    # Print front of queue
    def queueFront(self):
        if (self.front == self.rear):
            print("\nQueue is Empty")
        print("\nFront Element is:",
              self.queue[self.front])

def main():
    s = QueueArray()
    s.queueEnqueue(5)
    print(s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()


