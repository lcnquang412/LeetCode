class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        return None

    def peek(self) -> int:
        if self.queue:
            return self.queue[0]
        return None

    def empty(self) -> bool:
        return False if self.queue else True


myQueue = MyQueue()
print(myQueue.push(1))
print(myQueue.push(2))
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
