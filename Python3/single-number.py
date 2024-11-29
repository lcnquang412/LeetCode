class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        return list(hashmap.keys())[list(hashmap.values()).index(1)]


a = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber(a))
