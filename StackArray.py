# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Stack-Array
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 5: Implementing ADTs

class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

    def peek(self):  # return array top as peek
        return self.array[self.top]

    def pop(self):  # decreases top item and returns it
        if (self.is_empty()):
            return None
        item = self.array[self.top]
        self.top = self.top - 1
        return item

    def push(self, data=None): # push when array isn't full
        if (self.is_full()):
            return None
        self.top = self.top + 1
        self.array[self.top] = data
        newArr = [0 for i in range(self.size() + 1)]
        for i in range(0, self.size() - 1):
            newArr[i] = self.array[i]

        newArr[self.size() - 1] = data
        self.array = newArr

        return None

    def print(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")

    def is_empty(self):  # returns -1 if it is empty
        return (self.top == -1)

    def is_full(self):  # returns -1 if it is full
        return self.top == len(self.array) - 1

    def clear(self):  # delete all elements in array
        for i in range(0, self.top):
            self.array[self.top] == None
            self.top = self.top - 1
        self.top = -1
        return

    def size(self): # gets the size
        return self.top + 11

def main():
    s = StackArray(5)
    le = []
    la = []
    for i in range(20, 201, 10):
        s.push(i)
        le.insert(0, i)
    while not s.is_empty():
        la.append(s.pop())
    print(le == la)

# Don't run main on import
if __name__ == "__main__":
    main()
