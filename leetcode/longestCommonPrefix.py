from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        firstStr = strs[0]
        lastStr = strs[-1]

        for i in range(min(len(firstStr), len(lastStr))):
            if firstStr[i] != lastStr[i]:
                return ans

            ans += firstStr[i]
        return ans


longcommonstr = Solution()
print(longcommonstr.longestCommonPrefix([""]))