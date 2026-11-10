
class Solution:
    def vowelCount(self, s):
        vowels = 0
        consonants = 0

        for ch in s.lower():
            if ch.isalpha():
                if ch in "aeiou":
                    vowels += 1
                else:
                    consonants += 1

        return vowels, consonants
