**The Goal:** Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

- **Design:** I used mergesort for efficiency. Firstly, I sorted list with mergesort() and then assign this elements to two variables with iterating on items. 
- **Time Complexity:** O(nlogn) by ergesort algorithm.
- **Space Complexity:** O(n) for sorted list.