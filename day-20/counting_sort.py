class Solution:
    def countSort(self, arr):
        count = [0] * 26

        for ch in arr:
            count[ord(ch) - ord('a')] += 1

        ans = ""

        for i in range(26):
            while count[i] > 0:
                ans += chr(i + ord('a'))
                count[i] -= 1

        return ans