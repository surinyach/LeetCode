from collections import deque

class MinStack(object):

    def __init__(self):
        self.stack = deque()
        self.minstack= deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)
        else:
            self.minstack.appendleft(val)

        self.stack.append(val)
        
    def pop(self):
        """
        :rtype: None
        """
        val = -float("inf")
        if self.stack:
            val = self.stack.pop()

        if self.minstack and val == self.minstack[-1]:
            self.minstack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else 0 
    
    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack:
            return self.minstack[-1]
        else:
            return 0
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time Complexity: All the operations run in O(1) time