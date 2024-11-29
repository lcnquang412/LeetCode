class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashMap1 = {}
        hashMap2 = {}
        result = []
        for num in nums1:
            if num not in hashMap1:
                hashMap1[num] = 1
            else:
                hashMap1[num] += 1

        for num in nums2:
            if num not in hashMap2:
                hashMap2[num] = 1
            else:
                hashMap2[num] += 1

        for num in hashMap1:
            if num in hashMap2:
                minAppear = min(hashMap1[num], hashMap2[num])
                for i in range(minAppear):
                    result.append(num)

        return result


a = [1, 2, 2, 1]
b = [2, 2]
solution = Solution()
print(solution.intersect(a, b))
