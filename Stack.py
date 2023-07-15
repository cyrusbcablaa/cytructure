class Stack():

    def __init__(self, elements) :
        self.stack = []
        for i in elements:
            self.stacked = self.stack.append(i)
        self.stacked

    def push(self, push_elements):
        self.stack.extend(push_elements)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def __repr__(self) :
        return str(self.stack)
      
li = Stack([1,2,3,4])
li.push([5,10])
li.peek()
print(li.peek())