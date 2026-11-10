
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(sentence)

        if len(letters) == 26:
            return True
        else:
            return False


# Example
obj = Solution()
print(obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(obj.checkIfPangram("leetcode"))
