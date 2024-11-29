# Original
#         stack = []
#         index = -1
#         if len(s) == 0 or len(s) == 1:
#             return False
#         if s[0] == ")" or s[0] == "]" or s[0] == "}":
#             return False
#         for char in s:
#             if char == "(" or char == "[" or char == "{":
#                 stack.append(char)
#                 index += 1
#             elif index >= 0:
#                 if (char == ")" and stack[index] == "(") or \
#                         (char == "]" and stack[index] == "[") or \
#                         (char == "}" and stack[index] == "{"):
#                     stack.pop()
#                     index -= 1
#                 else:
#                     return False
#             else:
#                 return False
#         return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack


# a = "()[]{}"
# a = "([)]"
# a = "(){}}{"
# a = "[])"
a = "()"
solution = Solution()
print(solution.isValid(a))
