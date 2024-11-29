class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap[num] = True
        return False


a = [1, 2, 3, 1]
a = [1, 2, 3, 4]
a = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
solution = Solution()
print(solution.containsDuplicate(a))
