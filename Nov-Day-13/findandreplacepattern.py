
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def isMatch(word, pattern):
            map1 = {}
            map2 = {}

            for i in range(len(word)):
                a = word[i]
                b = pattern[i]

                if a in map1:
                    if map1[a] != b:
                        return False
                else:
                    map1[a] = b

                if b in map2:
                    if map2[b] != a:
                        return False
                else:
                    map2[b] = a

            return True

        result = []

        for word in words:
            if isMatch(word, pattern):
                result.append(word)

        return result