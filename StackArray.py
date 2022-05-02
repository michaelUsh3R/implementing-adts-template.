# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Stack-Array
#
# NAME:         FIXME
# ASSIGNMENT:   Project 5: Implementing ADTs

class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

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
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        # FIXME
        return

    def is_full(self):
        return self.top == len(self.array) - 1

    def clear(self):
        # FIXME
        return

    def size(self):
        return self.top + 1


def main():
    s = StackArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 10):
        s.push(i)
    s.print()
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

