# Python Modules and Packages - Notes

## Overview

Modular programming in Python involves splitting code into **modules** and **packages** for simplicity, maintainability, and reusability.

---

## Modules

### What is a Module?
- A module is a Python file containing definitions and statements.
- Can be built-in, written in C, or written in Python.

### Creating a Module
- Simply save a Python file with a `.py` extension.

```python
# mod.py
s = "Hello World"
a = [1, 2, 3]
def foo(arg):
    print(arg)
class Foo:
    pass
```

### Importing Modules

```python
import mod
from mod import s, foo
from mod import s as string
import mod as mymod
```

### The `dir()` Function
- Lists defined names in a module or current namespace.

### Module Search Path
- Uses `sys.path`
- Add paths using `sys.path.append()`

### Executing Module as Script
```python
if __name__ == "__main__":
    # Code to execute when run directly
```

### Reloading a Module
```python
import importlib
importlib.reload(mod)
```

---

## Packages

### What is a Package?
- A collection of modules in directories with `__init__.py` file.

### Importing From Packages
```python
import pkg.mod1
from pkg import mod1
from pkg.mod1 import foo
```

### `__init__.py`
- Executed on package import.
- Can contain initialization code.
- Optional since Python 3.3 (namespace packages).

### Importing *
- Define `__all__` in `__init__.py` to control exposed modules.

```python
__all__ = ['mod1', 'mod2']
```

### Subpackages
- Packages can contain subpackages.
- Nested imports use dot notation.

```python
from pkg.sub_pkg1.mod1 import foo
```

### Absolute vs Relative Imports
- Use `from .. import mod` for relative imports.

---

## Best Practices

- Avoid `from module import *` in production.
- Use `__name__ == '__main__'` for script behavior.
- Use `__all__` to control wildcard imports.
- Reload modules with care using `importlib.reload()`.

---

Happy Pythoning! 🐍