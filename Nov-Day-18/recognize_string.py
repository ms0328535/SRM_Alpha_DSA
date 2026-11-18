import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        max_heap = []

        for char, freq in count.items():
            heapq.heappush(max_heap, (-freq, char))

        result = []
        prev_freq = 0
        prev_char = ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)

            result.append(char)

            if prev_freq < 0:
                heapq.heappush(
                    max_heap, (prev_freq, prev_char)
                )

            prev_freq = freq + 1
            prev_char = char

        if len(result) != len(s):
            return ""

        return "".join(result)
