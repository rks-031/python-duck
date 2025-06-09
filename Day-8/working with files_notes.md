
# Working With Files in Python 🐍

This guide provides a summary of essential operations for working with files and directories in Python, including reading/writing, traversing directories, handling archives, and more.

## Table of Contents
- [Working With Files in Python 🐍](#working-with-files-in-python-)
  - [Table of Contents](#table-of-contents)
  - [1. Reading \& Writing Files](#1-reading--writing-files)
  - [2. Directory Listings](#2-directory-listings)
  - [3. Traversing Directories](#3-traversing-directories)
  - [4. File \& Directory Management](#4-file--directory-management)
    - [Deleting](#deleting)
    - [Creating](#creating)
  - [5. Copying, Moving, Renaming](#5-copying-moving-renaming)
  - [6. Archiving](#6-archiving)
    - [ZIP](#zip)
    - [TAR](#tar)
  - [7. Reading Multiple Files](#7-reading-multiple-files)
  - [🧭 Conclusion](#-conclusion)

---

## 1. Reading & Writing Files

Use Python’s `with open(...) as f:` pattern for safe file access:

```python
with open('data.txt', 'r') as f:
    data = f.read()

with open('output.txt', 'w') as f:
    f.write("Some data")
```

This ensures files are properly closed after usage.

---

## 2. Directory Listings

- Legacy: `os.listdir(path)`
- Modern: `os.scandir(path)` → includes metadata
- `pathlib.Path` offers `Path.glob('*.ext')`

```python
import os
for entry in os.scandir('my_directory/'):
    print(entry.name, entry.stat().st_size)
```

Pattern matching with `fnmatch` or `glob`:

```python
import fnmatch
fnmatch.filter(os.listdir('.'), '*.txt')

from pathlib import Path
for f in Path('.').glob('*.py'):
    print(f)
```

---

## 3. Traversing Directories

Use `os.walk()` to recursively traverse directory trees:

```python
import os
for dirpath, dirnames, filenames in os.walk('.'):
    print('Directory:', dirpath)
    for f in filenames:
        print('  File:', f)
```

---

## 4. File & Directory Management

### Deleting
- Files: `os.remove(path)`, `os.unlink(path)`, or `Path.unlink()`
- Directories: `os.rmdir(path)`, recursive deletion via `shutil.rmtree()`

### Creating
- Single dir: `os.mkdir(path)` or `Path(path).mkdir()`
- Nested dirs: `os.makedirs(path)` or `Path(path).mkdir(parents=True, exist_ok=True)`

---

## 5. Copying, Moving, Renaming

Use `shutil` for high-level file operations:

```python
import shutil

# Copy files:
shutil.copy(src, dst)
shutil.copy2(src, dst)  # preserves metadata

# Move or rename:
shutil.move(src, dst)
```

---

## 6. Archiving

### ZIP
```python
import zipfile

# Read:
with zipfile.ZipFile('archive.zip', 'r') as z:
    z.extractall()

# Write:
with zipfile.ZipFile('new.zip', 'w') as z:
    z.write('file.txt')
```

### TAR
```python
import tarfile

# Extract:
with tarfile.open('archive.tar.gz') as t:
    t.extractall()

# Create:
with tarfile.open('new.tar.gz', 'w:gz') as t:
    t.add('folder/')
```

---

## 7. Reading Multiple Files

Use the `fileinput` module to iterate through multiple files as a single stream:

```python
import fileinput

for line in fileinput.input(['file1.txt', 'file2.txt']):
    process(line)
```

---

## 🧭 Conclusion

Using built-in modules (`os`, `pathlib`, `shutil`, `zipfile`, `tarfile`, `fileinput`), you can:

- Handle basic I/O (read/write)
- Navigate and manage directories
- Copy, move, rename, delete files/dirs
- Create/extract archives
- Seamlessly read multiple file sources

These combined form a powerful file-manipulation toolkit in Python.
