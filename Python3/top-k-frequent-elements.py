class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        hashMap = {}
        hashMapArr = []
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        for key in hashMap:
            hashMapArr.append({
                "key": key,
                "value": hashMap[key]
            })
        hashMapArrSorted = sorted(hashMapArr, key=lambda j: j['value'], reverse=True)
        # print(hashMapArrSorted)

        for i in range(k):
            result.append(hashMapArrSorted[i]['key'])

        return result


a = [1, 1, 1, 2, 2, 3]
b = 2
solution = Solution()
print(solution.topKFrequent(a, b))
