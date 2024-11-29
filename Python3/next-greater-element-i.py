class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashMap = {}
        resultArr = []

        for i in range(len(nums2) - 1):
            num = nums2[i]
            numNext = -1
            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    numNext = nums2[j]
                    break
            hashMap[num] = numNext

        for i in range(len(nums1)):
            num = nums1[i]
            result = -1
            if num in hashMap:
                result = hashMap[num]
            resultArr.append(result)

        return resultArr


a = [4, 1, 2]
b = [1, 3, 4, 2]
a = [2, 4]
b = [1, 2, 3, 4]
a = [1, 3, 5, 2, 4]
b = [6, 5, 4, 3, 2, 1, 7]
solution = Solution()
print(solution.nextGreaterElement(a, b))
