"""
File Name: recursive_stack.py
Description: recursive implementation of the stack class to be used in the main file
"""

###############
# Stack Class #
###############
class Stack():                                                                                # Creates Stack class to contain item methods                                                                                                                                   
    def __init__(self, name):                                                                 # Class contains items, names, and moves
        self.items = []                                                                       # Items begin as an empty list
        self.moves = 0                                                                        # Each item's moves are set at 0 to begin
        self.name = name
    def __str__(self):
        string = ""
        for i in self.items:
            string += str(i) + " "
        return string                                                                         # Returns string of each item in list of items
    def size(self):                                                                           # Returns size of item's list
        return len(self.items)
    def push(self, item):                                                                     # Appends item to items list
        self.items.append(item)
    def pop(self):                                                                            # Pops item from list of items
        return self.items.pop()
    def peek(self):                                                                           # Returns last item in list of items
        return self.items[-1]