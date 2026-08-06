# DSA-Journey-
A structured repository of Python solutions to Striver's A2Z DSA Sheet, showcasing my problem-solving journey, coding consistency, and interview preparation.

📊 SUMMARY

- Problems Solved:14
- Current Topic: Arrays
- Language: Python
- Platform: LeetCode + Striver A2Z
- Goal: 200+ Problems

 
📊 DSA Progress Tracker

| # | Problem Name | Topic | Time Taken | Attempts | Status |
|:-:|--------------|:-----:|:----------:|:--------:|:------:|
| 1 | Largest Element in an Array | Arrays | 12 min | 1 | ✅ Solved |
| 2 | Largest Digit in a Number | Basic Maths | 15 min | 2 | ✅ Solved |
| 3 | Count Digits | Basic Maths | 25 min | 2 | ✅ Solved |
| 4 | Reverse Array | Arrays | 30 min | 2 | ✅ Solved |
| 5 | Left Rotate Array by One | Arrays | 1 hr 20 min | 4 | ✅ Solved |
| 6 | Move Zeroes | Arrays | 3 hrs | 6 | ✅ Solved |
| 7	| Rotate Array by K	| Arrays	| 2 hrs	| 8	| ✅ Solved |
| 8 | Leaders in an Array | Arrays | 1 hr | 5 | ✅ Solved |
| 9 | Maximum Subarray Sum (Kadane's Algorithm) | Arrays | 1hr | 3 | ✅ Solved |
| 10 | Next Permutation | Arrays | 1 hr | 4 | ✅ Solved |
| 11 | Two Sum | Arrays, Hashing | 25 min | 3 | ✅ Solved |
| 12 | Container With Most Water | Two Pointers | 30 min | 3 | ✅ Solved |
| 13 | Best Time to Buy and Sell Stock | Arrays | 15 min | 1 | ✅ Solved |
| 14 | Majority Element | Arrays, Hashing, Boyer-Moore Voting Algorithm | 55 min | 5 | ✅ Solved (HashMap + Boyer-Moore) |
| 15 | Longest Consecutive Sequence | Arrays, HashSet | 35 min | 4 | ✅ Solved |
---

🧠 Learning Journal

| Problem | Challenges Faced | What I Learned |
|----------|------------------|----------------|
| Largest Element in an Array | Initially struggled to keep track of the maximum value while traversing the array. | Learned how to maintain a running maximum using a single traversal with **O(n)** time complexity. |
| Largest Digit in a Number | Confused about comparing digits while extracting them from a number. | Learned digit extraction using modulo (`%`), floor division (`//`), and maintaining the maximum digit during traversal. |
| Count Digits | Confused about loop termination and reducing the number after extracting digits. | Learned digit extraction using modulo (`%`) and floor division (`//`) while understanding loop conditions. |
| Reverse Array | Difficulty understanding how swapping works without losing data. | Learned in-place swapping using a temporary variable and gained confidence with index manipulation. |
| Left Rotate Array by One | Confused about shifting elements, temporary storage, and array indexing. | Learned how to shift array elements correctly, preserve values using a temporary variable, and perform in-place rotation. |
| Move Zeroes | Mixed up indices with values, struggled with swapping logic, nested loops, `break`, and encountered **Time Limit Exceeded (TLE)**. | Learned the difference between indices and values, improved debugging skills, understood swapping thoroughly, and realized why brute-force approaches can fail due to time complexity. |
| Rotate Array by K | Initially struggled to understand the reverse approach, confused indices with slices, and had never used helper functions before. Faced issues with index ranges (k-1, n-1), in-place modification, and implementing the reverse logic correctly. | Learned the optimal Reverse Algorithm for array rotation, understood helper (nested) functions, strengthened two-pointer concepts, practiced in-place array manipulation, learned why k = k % n is required, and improved debugging by fixing logic instead of relying on brute force. |
| Leaders in an Array | Initially confused about traversing from right to left, range() syntax with a negative step, difference between index and value (nums[i]), list operations (append, reverse), and indentation. Also reset current_max inside the loop by mistake and overwrote the leaders list instead of adding to it. | Learned the optimal O(n) approach using right-to-left traversal, maintaining a running maximum, correctly using append() and reverse(), and debugging logical errors caused by loop placement and Python syntax. |
| Maximum Subarray Sum (Kadane's Algorithm) | Initially tried using `sum()`, got confused about the `range()` start index, mixed up updating `curr_sum` and `max_sum`, added unnecessary conditions, and faced indentation errors while implementing the algorithm. | Learned Kadane's Algorithm from first principles: maintain `current_sum` and `maximum_sum`, decide at each element whether to continue the current subarray or start a new one, initialize both with the first element, iterate from index `1`, and achieve the optimal `O(n)` solution. |
| Next Permutation | Initially struggled with understanding lexicographical order, pivot identification, and implementing the algorithm correctly. Faced issues with Python syntax (`=` vs `==`), in-place swapping, and reversing only the suffix. | Learned how to derive the Next Permutation algorithm from scratch, identify the pivot using right-to-left traversal, find the next greater element, perform in-place swapping, reverse only the suffix, and debug Python implementation errors effectively. |
| Two Sum | Initially thought of checking adjacent elements and using brute force. Struggled with understanding when to store elements in the HashMap, dictionary membership checking (`in`), loop boundaries, and Python syntax while implementing the solution. | Learned to optimize the brute-force approach from `O(n²)` to `O(n)` using a HashMap. Understood the concept of storing `value → index`, finding the complement using `target - nums[i]`, checking if it already exists in the HashMap, and returning the indices when found. Also improved confidence in implementing HashMap-based solutions in Python. |
| Container With Most Water | Initially thought both pointers should move together and was confused about updating the maximum area. Also mixed up indices with heights while calculating the area. | Learned the Two Pointer approach by understanding that the area is determined by the minimum of the two heights and the distance between them. Understood why only the pointer with the smaller height should move, how to update the maximum area using `max()`, and the importance of using heights instead of indices in the area calculation. |
| Best Time to Buy and Sell Stock | Initially tried thinking about the largest selling price instead of tracking the minimum buying price. Also made a loop boundary mistake by skipping the last element. | Learned the optimal O(n) approach by maintaining the minimum price seen so far and calculating the profit for each day. Understood how to update the maximum profit using `max(max_profit, profit)` and why every element, including the last one, must be traversed. |
| Majority Element | Initially understood the brute-force idea but struggled to implement the HashMap approach by confusing a single count variable with per-element frequencies. Later found Boyer-Moore Voting Algorithm confusing, especially the candidate update when `count == 0` and why `elif` is required instead of another `if`. | Learned two optimal approaches. First, the HashMap solution by storing `value → count` and returning the element once its frequency exceeds `n/2`. Then understood the Boyer-Moore Voting Algorithm by maintaining only a `candidate` and a `count`, where different elements cancel each other out. Also learned why Boyer-Moore returns a candidate that should be verified with a second pass if a majority element is not guaranteed to exist. |
| Longest Consecutive Sequence | Initially tried using indices instead of actual numbers, was confused about when to start a sequence, and made indentation mistakes with the `while` loop. Also took time to understand why sequences should only start when `num - 1` is not present in the HashSet. | Learned to optimize the solution from a repeated traversal approach to an O(n) solution using a HashSet. Understood how HashSet provides O(1) lookups, why duplicate elements are automatically removed, and why checking `num - 1` prevents counting the same sequence multiple times. Also learned to expand a sequence using `while curr + 1 in hashset` and update the maximum sequence length correctly. |
