
class Solution:
    def longestCommonSuffix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        suffix = strs[0]

        for i in range(1, len(strs)):
            j = 1

            while (j <= len(suffix) and
                   j <= len(strs[i]) and
                   suffix[-j] == strs[i][-j]):
                j += 1

            suffix = suffix[len(suffix) - j + 1:]

            if suffix == "":
                return ""

        return suffix
