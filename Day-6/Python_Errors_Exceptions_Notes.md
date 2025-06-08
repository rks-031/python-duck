# 📘 Python Errors and Exceptions – Notes

## 📖 Table of Contents
- [📘 Python Errors and Exceptions – Notes](#-python-errors-and-exceptions--notes)
  - [📖 Table of Contents](#-table-of-contents)
  - [🐍 Introduction to Exceptions](#-introduction-to-exceptions)
  - [❌ Syntax Errors vs Exceptions](#-syntax-errors-vs-exceptions)
  - [🚨 Raising Exceptions](#-raising-exceptions)
  - [🛠️ Using `assert` for Debugging](#️-using-assert-for-debugging)
  - [🧱 Handling Exceptions with `try` and `except`](#-handling-exceptions-with-try-and-except)
    - [Basic Usage:](#basic-usage)
    - [Specific Exception Example:](#specific-exception-example)
    - [Multiple Exceptions:](#multiple-exceptions)
  - [➕ Using `else` in Exception Handling](#-using-else-in-exception-handling)
  - [♻️ Using `finally` for Cleanup](#️-using-finally-for-cleanup)
  - [🧩 Creating Custom Exceptions](#-creating-custom-exceptions)
  - [✅ Conclusion](#-conclusion)

---

## 🐍 Introduction to Exceptions
- **Exceptions** occur during execution when syntactically correct code results in an error.
- Exceptions provide a mechanism for error handling in Python.
- Common keywords: `try`, `except`, `else`, `finally`, `raise`, `assert`.

---

## ❌ Syntax Errors vs Exceptions
- **Syntax Error**: Detected during parsing (e.g., unmatched parentheses).
- **Exception**: Raised during runtime (e.g., `ZeroDivisionError`, `FileNotFoundError`).

Example:

```python
# Syntax Error
print(0 / 0))

# Exception
print(0 / 0)  # Raises ZeroDivisionError
```

---

## 🚨 Raising Exceptions
- Use `raise` to trigger exceptions manually.

```python
number = 10
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
```

---

## 🛠️ Using `assert` for Debugging
- Use `assert` to validate conditions during development.

```python
number = 10
assert number <= 5, f"The number should not exceed 5. ({number=})"
```

- Note: `assert` is disabled when running Python with optimization (`-O` flag).

---

## 🧱 Handling Exceptions with `try` and `except`

### Basic Usage:

```python
try:
    risky_function()
except SomeException as e:
    print(f"Error occurred: {e}")
```

### Specific Exception Example:

```python
try:
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
```

### Multiple Exceptions:

```python
try:
    operation1()
    operation2()
except FileNotFoundError:
    print("File not found.")
except RuntimeError as e:
    print("Runtime issue:", e)
```

---

## ➕ Using `else` in Exception Handling
- Runs only if the `try` block didn't raise an exception.

```python
try:
    check_system()
except RuntimeError as e:
    print(e)
else:
    print("System check passed.")
```

---

## ♻️ Using `finally` for Cleanup
- Runs regardless of whether an exception occurred.

```python
try:
    operation()
except SomeException:
    print("Handled the error.")
finally:
    print("Cleanup complete.")
```

---

## 🧩 Creating Custom Exceptions
- Subclass from `Exception`.

```python
class PlatformException(Exception):
    '''Custom exception for platform issues.'''

def linux_only_function():
    import sys
    if "linux" not in sys.platform:
        raise PlatformException("Only runs on Linux.")
```

---

## ✅ Conclusion
Python provides powerful tools for handling exceptions:
- Use `try` / `except` to handle errors gracefully.
- Add `else` for code to run only when no exceptions occur.
- Use `finally` to always execute cleanup actions.
- Customize exceptions for domain-specific error handling.
