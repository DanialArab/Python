## Coding Interview Tips and Tricks

1. When we need a contiguous subarray, we need to think of a sliding window. for example, 
2. When the question talks about subsequence, which is not contiguous, we may not need sliding window and maybe counter works.

1- Contiguous subarrays → Sliding Window

If a problem asks for a contiguous subarray of size k or with some sum/average/maximum property, sliding window is often the optimal approach.

Example: <a href="https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=problem-list-v2&envId=sliding-window">LEETCODE 643. Maximum Average Subarray I</a>

2- Subsequence (not contiguous) → Counting / Hashing

If a problem allows picking elements from anywhere (subsequence), you may not need a sliding window.

Frequency counting (Counter) or other aggregation techniques often work better.

Example: <a href="https://leetcode.com/problems/longest-harmonious-subsequence/description/">LEETCODE 594. Longest Harmonious Subsequence</a>
