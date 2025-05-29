- Functional Programming Learnings
  1. Keep your data and function independent
  2. avoid changing state of variables, instead declare others
  3. accept function/reference as a param
  
- Programmed a data processing pipeline
   
## Comparison b/w procedural and functional approaches

🧱 Procedural Programming in Python

✅ Concept:

Follows a step-by-step set of instructions (procedures).

Code is organized into functions and blocks that modify global state or variables.

Focus is on how to do things (control flow).

🧾 Example:
```python
def sum_of_squares(numbers):
    result = 0
    for num in numbers:
        result += num * num
    return result

print(sum_of_squares([1, 2, 3, 4]))
```
✅ Pros:

 - Easy to understand for beginners.
 - Explicit control over flow and variables.
 - Better for small scripts and algorithms with stepwise logic.

❌ Cons:

 - Can become messy for larger programs (spaghetti code).
 - Relies on mutable state — harder to debug or test.
 - Less reusable — more repetition. 

---

🧮 Functional Programming in Python

✅ Concept:

Code is built using pure functions (no side effects).

Avoids changing state and mutable data.

Focus is on what to do, not how.

🧾 Example:
```python
from functools import reduce

numbers = [1, 2, 3, 4]
squares = map(lambda x: x * x, numbers)
total = reduce(lambda acc, x: acc + x, squares)
print(total)
```
✅ Pros:

 - Easier to test/debug due to stateless functions.
 - More concise, especially with map(), filter(), reduce().
 - Encourages reusability and modular design.
 - Aligns well with parallel or concurrent execution.

❌ Cons:
 - Can be harder to read for newcomers.
 - May involve many intermediate function calls.
 - Python isn't a pure functional language, so some functional patterns can be less efficient.

