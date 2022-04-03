**The Goal:** For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

- **Time Complexity:** O(n), Trie approach determited the time complexity
- **Space Complexity:** O(n). We only keep caaracters of words but not for every character. So, space complexity linear but depends on path_block count, path_block list length, unique path_block list element count.


**RouteTrie Class**

Method 1 : insert
- **Time Complexity:** O(n). 'For loop' time complexity depends on the iterating object length.
- **Space Complexity:** O(n)

Method 2 : find
- **Time Complexity:** O(n). 'For loop' time complexity depends on the iterating object length.
- **Space Complexity:** O(n)


**RouteTrieNode Class**

Method 1 : insert

- **Time Complexity:** O(1). Only for one item.
- **Space Complexity:** O(1)


**Router Class**

Method 1 : add_handler
- **Time Complexity:** O(1). Only for one item.
- **Space Complexity:** O(1)

Method 2 : lookup
- **Time Complexity:**  O(n). Worksnly for one item: O(1). The 'find' method inside this method time complexity is O(n).
- **Space Complexity:** O(n)

Method 3 : split_path
- **Time Complexity:**  O(n). 'For loop' time complexity depends on the iterating object length.
- **Space Complexity:** O(n)