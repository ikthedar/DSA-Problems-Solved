class MinStack:

    # We will be creating two stack using arrays;
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        # we will take the input value and add that to the first stack
        self.stack.append(val)
        
        # we need to know if there is already a value added to the min stack
        # take the minimum of (the inpute value and top value of minstack)
        # then append the value to minStack
        
        # update our value first
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
