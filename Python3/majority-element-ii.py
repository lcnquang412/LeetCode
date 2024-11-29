class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count1 = count2 = 0
        majority1 = majority2 = -1000000001
        for num in nums:
            if num == majority1:
                count1 += 1
            elif num == majority2:
                count2 += 1
            elif count1 == 0:
                majority1 = num
                count1 = 1
            elif count2 == 0:
                majority2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == majority1:
                count1 += 1
            elif num == majority2:
                count2 += 1

        result = []
        # print(majority1)
        # print(majority2)
        if count1 > len(nums) // 3:
            result.append(majority1)
        if count2 > len(nums) // 3:
            result.append(majority2)
        return result


# a = [3, 2, 3]
# a = [1, 2]
a = [1, 2, 3]
a = [3, 3, 4]
a = [2, 1, 1, 3, 1, 4, 5, 6]
solution = Solution()
print(solution.majorityElement(a))
