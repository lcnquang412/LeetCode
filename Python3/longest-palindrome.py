class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 1
        result = 0
        hasOdd = False
        hashMap = {}
        for char in s:
            hashMap[char] = 1 if char not in hashMap else hashMap[char] + 1
        for char in hashMap:
            count = hashMap[char]
            if count % 2 == 0:
                result += count
            else:
                hasOdd = True
                if count > 1:
                    result += count - 1
        return result + 1 if hasOdd else result


a = "abccccdd"
a = "a"
a = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
solution = Solution()
print(solution.longestPalindrome(a))
