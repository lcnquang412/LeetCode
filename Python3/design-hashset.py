class Solution:
    def __init__(self):
        self.set = {}

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        if key in self.set:
            del self.set[key]

    def contains(self, key: int) -> bool:
        return key in self.set


obj = Solution()
obj.add(1)
obj.add(2)
obj.add(2)
print(obj.contains(2))
print(obj.set)
