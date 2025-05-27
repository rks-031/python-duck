## Learnings and Challenges
- Implemented Contact Management System using Dictonary
- Went through documentations of List, Tuples, and Dictionaries
- Solved LeetCode problems: Valid Anagrams and Group Anagrams
- Compared efficiency of different data structures for various operations

## Efficiency of different data structures
| Operation                     | List           | Tuple                        | Dictionary               |
| ----------------------------- | -------------- | ---------------------------- | ------------------------ |
| Indexing (e.g., `a[i]`)       | O(1)           | O(1)                         | O(1) (via key)           |
| Iteration                     | O(n)           | O(n)                         | O(n)                     |
| Search (in / not in)          | O(n)           | O(n)                         | O(1) average, O(n) worst |
| Insertion (end)               | O(1) amortized | (immutable)                | O(1)                     |
| Insertion (middle)            | O(n)           |                            | O(1)                     |
| Deletion (by value/index)     | O(n)           |                            | O(1)                     |
| Memory usage                  | Higher         | Lower                        | Higher                   |

