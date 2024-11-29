class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in hashMap:
                if abs(hashMap[num] - i) <= k:
                    return True
            hashMap[num] = i
        return False


a = [1, 2, 3, 1]
b = 3
# a = [1, 0, 1, 1]
# b = 1
# a = [1, 2, 3, 1, 2, 3]
# b = 2
solution = Solution()
print(solution.containsNearbyDuplicate(a, b))
