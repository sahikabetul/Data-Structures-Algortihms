- **Time Complexity:** O(n*l). n: number of words, l: average length of the word.
- **Space Complexity:** O(n). We only keep characters of words but not for every character. So, space complexity linear but depends on word count, word length.

**Trie Class**
Method 1 : insert
- **Time Complexity:** O(n). 'For loop' time complexity depends on the iterating object length.
- **Space Complexity:** O(n)

Method 2 : find
- **Time Complexity:** O(n). 'For loop' time complexity depends on the iterating object length.
- **Space Complexity:** O(n)

**TrieNode Class**
Method 1 : insert
- **Time Complexity:** O(1). Only for one item.
- **Space Complexity:** O(1)

Method 2 : suffixes
- **Time Complexity:** O(n). 'For loop' time complexity depends on the iterating object length.
- **Space Complexity:** O(n)