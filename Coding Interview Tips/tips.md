## Coding Interview Tips and Tricks

1- Contiguous subarrays → Sliding Window

If a problem asks for a contiguous subarray of size k or with some sum/average/maximum property, sliding window is often the optimal approach.

Example: <a href="https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=problem-list-v2&envId=sliding-window">LEETCODE 643. Maximum Average Subarray I</a>

2- Subsequence (not contiguous) → Counting / Hashing

If a problem allows picking elements from anywhere (subsequence), you may not need a sliding window.

Frequency counting (Counter) or other aggregation techniques often work better.

Example: <a href="https://leetcode.com/problems/longest-harmonious-subsequence/description/">LEETCODE 594. Longest Harmonious Subsequence</a>




Some tips:
- Always begin by asking clarifying questions about the prompt.
- Talk through your approach before coding—outline candidate solutions and tradeoffs. Recruiters expect clear thinking, not just correct code
- After coding, walk through test cases, including edge and corner cases. If bugs emerge, debug them live and explain why they occurred and how you fix them
   - If your code fails a test case: just calmly add a print, inspect the logic, and explain the fix
   - You can say something like: “Let’s try a few test cases before I run this. For input [2, 3, 3, 2, 4], I expect output 4, because it’s the only non-repeating number.” and “Edge case: empty list → should return None or -1, depending on the requirement.”
- Discuss time/space complexity and mention tradeoffs (e.g. readability vs performance) to showcase awareness.



Great resource: 
- https://www.youtube.com/watch?v=0K_eZGS5NsU
- for prep: https://neetcode.io/
- prep with Coderpad sandbox: https://coderpad.io/resources/docs/for-candidates/interview-preparation-guide/
- drawing on Coderpad: https://coderpad.io/resources/docs/interview/drawing-mo
