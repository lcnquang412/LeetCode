class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for operation in operations:
            length = len(stack)
            if operation == "+":
                if length > 1:
                    stack.append(stack[length - 1] + stack[length - 2])
            elif operation == "D":
                if length > 0:
                    stack.append(stack[length - 1] * 2)
            elif operation == "C":
                if length > 0:
                    stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)


a = ["5", "2", "C", "D", "+"]
solution = Solution()
print(solution.calPoints(a))
