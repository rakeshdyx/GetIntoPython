class Solution:
    def romanToInt(self, s: str) -> int:
        translations = { "I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000 }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and translations[s[i]] < translations[s[i+1]]:
                res -= translations[s[i]]
            else:
                res += translations[s[i]]
        return res


intVaule = Solution()

print(intVaule.romanToInt("IV"))

                     