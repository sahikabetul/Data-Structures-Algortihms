**The Goal:** Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

- **Design:** I keep three indexes: First for iterating over the input_list(i), second for keeping lastly placed 0's index (i0) and third for keeping lastly placed 2's index (i2). I set pivots by i and if necessary, swap with i0 or i2.
- **Time Complexity:** O(n). Single traversal
- **Space Complexity:** O(n). I used only one list.