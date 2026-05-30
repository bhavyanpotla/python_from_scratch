class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
         
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"
    
    def peek(self):
         
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

 

s = stack()            
s.push(10)             
s.push(20)             

print(s.peek())        
print(s.pop())         
print(s.size())        