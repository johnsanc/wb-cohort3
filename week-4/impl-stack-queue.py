from queue import LifoQueue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = LifoQueue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        top = self.stack.get()
        self.stack.put(top)
        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()