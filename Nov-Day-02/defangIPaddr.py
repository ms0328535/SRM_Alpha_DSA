
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        for ch in address:
            if ch == ".":
                result += "[.]"
            else:
                result += ch

        return result


address = "1.1.1.1"
obj = Solution()
print(obj.defangIPaddr(address))
