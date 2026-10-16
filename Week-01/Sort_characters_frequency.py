def frequency_sort(s: str) -> str:
    # Step 1: Manually build a frequency map
    freq_map = {}
    for char in s:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
            
    # Step 2: Convert dictionary to a mutable list of pairs [char, frequency]
    pairs = []
    for char, freq in freq_map.items():
        pairs.append([char, freq])
        
    # Step 3: Selection Sort custom-built to sort by frequency descending
    n = len(pairs)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            # Sort by frequency descending
            if pairs[j][1] > pairs[max_idx][1]:
                max_idx = j
        # Swap the pairs
        pairs[i], pairs[max_idx] = pairs[max_idx], pairs[i]
        
    # Step 4: Rebuild the result string from sorted pairs
    result = []
    for char, freq in pairs:
        result.append(char * freq)
        
    return "".join(result)

# Example Usage:
print(frequency_sort("tree"))   # Output: "eert" (or "eetr")
print(frequency_sort("cccaaa")) # Output: "cccaaa" (or "aaaccc")
