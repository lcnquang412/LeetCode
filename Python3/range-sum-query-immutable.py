class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.numsTotal = [0]
        total = 0
        for num in nums:
            total += num
            self.numsTotal.append(total)
            # print(self.numsTotal)

    def sumRange(self, left: int, right: int) -> int:
        return self.numsTotal[right + 1] - self.numsTotal[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
