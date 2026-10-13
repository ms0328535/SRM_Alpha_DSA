# Week 01: Data Structures and Algorithms

## Folder Contents & Summary

This folder contains my Week 01 coding activities, focusing on arrays, searching, duplicate detection, and two-pointer techniques.

| **S.No.** | **File** | **Approach** | **Time Complexity** | **Space Complexity** |
|---|---|---|---|---|
| 1 | [Container With Most Water](container_with_most_water.py) | I use two pointers, one at each end of the array. I calculate the area formed by the two heights, update the maximum area, and move the pointer with the smaller height inward. | O(N) | O(1) |
| 2 | [Finding Duplicates](finding_duplicates.py) | I check the elements of the collection to identify repeated values. A set can be used to track previously seen elements and detect duplicates efficiently. | O(N) average | O(N) |
| 3 | [Linear Search](linear_search.py) | I traverse the array from the beginning and compare each element with the target value. If a match is found, I return its position; otherwise, I report that the element is not present. | O(N) | O(1) |
| 4 | [Move Zeroes to End](moves_zero_end.py) | I use a pointer to place non-zero elements at the beginning of the array, then move the zeroes to the end while preserving the order of non-zero elements. | O(N) | O(1) |
| 5 | [Remove Duplicates](remove_duplicates.py) | I identify repeated elements and retain unique values. The two-pointer approach can remove duplicates in-place when the input array is sorted. | O(N) | O(1) |

**Note:** The complexity values above assume the approaches described in the table. Check your actual Python implementations, especially the duplicate-related programs, and update the complexities if your code uses a different approach.

## Learning Outcomes

- Understand array traversal and element searching.
- Apply sets to identify duplicate elements.
- Learn the two-pointer technique.
- Practice in-place array modification.
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
└── remove_duplicates.py
```
