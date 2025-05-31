- working with important maginc method: __init __() --> which is the contructor
- __repr__ method
- class vs static methods
- inheritance
- adding validation checks using **assert** statements
- getters and setters
- modularization
- oops principles
- design a stack with increment operation: leetcode problem
- design parking system: leetcode problem
- Implementation Challenge: Design a simple agent class structure with basic functionality
<br/>
### Class design decisions and tradeoffs:

1. Design Decisions

| Aspect               | Decision                                                                 |
|----------------------|--------------------------------------------------------------------------|
| **Class Attributes** | `agent_name`, `task`, and `todo_map` give the agent identity and purpose.|
| **Task Storage**     | Tasks are stored in a dictionary `todo_map` with the deadline (int) as the key and task (string) as the value. |
| **Deadline Format**  | Deadlines are stored as integers representing minutes from now for simplicity. |
| **Priority Sorting** | `show_priority_wise_todos()` sorts the tasks by deadline (ascending).   |
| **Interactive Input**| `ask_user()` uses `input()` to gather tasks from the user interactively. |


2. Tradeoff

| Advantage                               | Tradeoff                                                                 |
|----------------------------------------|--------------------------------------------------------------------------|
| ✅ Simple and easy to understand        | ❌ Only one task allowed per deadline (key overwrite risk in dictionary) |
| ✅ Fast sorting with built-in `sorted()`| ❌ No support for actual time or date comparisons                        |
| ✅ Lightweight and dependency-free      | ❌ No persistence: todos are lost when the program ends                  |
| ✅ Minimal code footprint               | ❌ No error handling (e.g., non-integer deadline input may crash)        |



