###################################
# Name: Jordan Belinsky           #
# Date: October 22nd, 2018        #
# File: iterativeStack.py         #
###################################

###############
# Stack Class #
###############
class Stack():                                                                                                                                                                                                           
    def __init__(self, name): 
        self.name=name                                                               
        self.items = []                                                                      
        self.moves = 0                                                                    
    def __str__(self):
        string = ""
        for i in self.items:
            string += str(i) + " "
        return string                                                                         
    def size(self):                                                                          
        return len(self.items)
    def push(self, item):                                                                 
        self.items.append(item)
    def pop(self):                                                                     
        return self.items.pop()
    def peek(self):                                                                          
        return self.items[-1]
    def viableMove(self, other, another):                                       
        if self.size() != 0 and (other.size() == 0 or self.peek() < other.peek()):           
            other.push(self.pop())                                                       
            another.moves += 1                                                              
        elif other.size() != 0 and (self.size() == 0 or other.peek() < self.peek()):         
            self.push(other.pop())                                                           
            another.moves += 1                                                                 
    