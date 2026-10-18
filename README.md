
# Week 01: Data Structures and Algorithms

## Folder Contents & Summary

This folder contains my Week 01 coding activities, focusing on arrays, searching, duplicate detection, two-pointer techniques, and sliding-window algorithms.

| **S.No.** | **File** | **Approach** | **Time Complexity** | **Space Complexity** |
|---|---|---|---|---|
| 1 | [Container With Most Water](container_with_most_water.py) | I use two pointers, one at each end of the array. I calculate the area formed by the two heights, update the maximum area, and move the pointer with the smaller height inward. | O(N) | O(1) |
| 2 | [Finding Duplicates](finding_duplicates.py) | I use a set to track previously seen elements and identify repeated values efficiently. | O(N) average | O(N) |
| 3 | [Linear Search](linear_search.py) | I traverse the array from the beginning and compare each element with the target value. If a match is found, I return its position; otherwise, I report that the element is not present. | O(N) | O(1) |
| 4 | [Move Zeroes to End](moves_zero_end.py) | I use a pointer to place non-zero elements at the beginning of the array, preserving their order and moving zeroes to the end. | O(N) | O(1) |
| 5 | [Remove Duplicates](remove_duplicates.py) | I identify repeated elements and retain unique values. A two-pointer approach can remove duplicates in-place when the input array is sorted. | O(N) | O(1) |
| 6 | [Contains Duplicate II](contains_duplicate_II.py) | I use a sliding window and a set to check whether any value appears more than once within a distance of at most K indices. | O(N) average | O(min(N, K)) |
| 7 | [Find All Anagrams in a String](find_all_anagrams.py) | I use character frequency counting and a fixed-size sliding window to find all substrings that are anagrams of the given pattern. | O(N + M)* | O(1)* |
| 8 | [Permutation in String](permutation_in_string.py) | I compare character frequencies in a fixed-size sliding window to determine whether the string contains a permutation of the given pattern. | O(N + M)* | O(1)* |
| 9 | [Max Consecutive Ones III](max_consecutive_ones_III.py) | I use a sliding window to count zeroes and shrink the window whenever the number of zeroes exceeds K. | O(N) | O(1) |
| 10 | [Longest Repeating Character Replacement](longest_repeating_character_replacement.py) | I use a frequency dictionary and maintain a running maximum frequency to determine how many replacements are required for a valid window. | O(N) average | O(U) |
| 11 | [Longest Substring Without Repeating Characters](longest_substring_without_repeating_characters.py) | I use a sliding window and a dictionary of last-seen indices to avoid repeated characters and find the longest substring without repeating characters. | O(N) average | O(U) |

**Note:** Complexity depends on the actual implementation. For the two string problems marked with an asterisk, the stated bounds assume a fixed lowercase English alphabet and optimized frequency counting. Python `Counter` comparisons may have different costs depending on the number of distinct characters.

## Learning Outcomes

- Understand array traversal and element searching.
- Apply sets and hash-based techniques to identify duplicates.
- Learn and implement the two-pointer technique.
- Practice in-place array modification.
- Understand fixed-size and variable-size sliding-window algorithms.
- Use character frequency counting to solve string problems.
- Track conditions efficiently while expanding and shrinking a window.
- Maintain a running maximum frequency when solving character replacement problems.
- Avoid recalculating character frequencies unnecessarily inside loops.
- Analyze time and space complexity.

## Language

Python 3

## Repository Structure

```text
Week-01/
├── README.md
├── container_with_most_water.py
├── finding_duplicates.py
├── linear_search.py
├── moves_zero_end.py
├── remove_duplicates.py
├── contains_duplicate_II.py
├── find_all_anagrams.py
├── permutation_in_string.py
├── max_consecutive_ones_III.py
├── longest_repeating_character_replacement.py
└── longest_substring_without_repeating_characters.py
```
