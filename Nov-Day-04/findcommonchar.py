
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = []

        for ch in set(words[0]):
            count = min(word.count(ch) for word in words)

            for i in range(count):
                result.append(ch)

        return result


# Example
obj = Solution()
words = ["bella", "label", "roller"]
print(obj.commonChars(words))
