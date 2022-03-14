**The Goal:** You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.
- **Design:** I implemented binary search tree technique. For this, I coded recursive_search() function for searching in branches.
- **Time Complexity:** O(logn) Binary search tree complexity.
- **Space Complexity:** O(1) Binary search tree takes constant space.