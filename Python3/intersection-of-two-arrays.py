class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashMap1 = {}
        hashMap2 = {}
        result = []
        for num1 in nums1:
            if num1 not in hashMap1:
                hashMap1[num1] = True
        for num2 in nums2:
            if num2 in hashMap1 and num2 not in hashMap2:
                result.append(num2)
                hashMap2[num2] = True
        return result


a = [1, 2, 2, 1]
b = [2, 2]
solution = Solution()
print(solution.intersection(a, b))
