
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

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