
# 📚 Rotate 2D Matrix - 90 Degrees Clockwise

Welcome to the **Rotate 2D Matrix** project! 🚀 This challenge is all about mastering matrix manipulation and in-place operations in Python. By completing this project, you’ll strengthen your understanding of nested lists, algorithms, and space-efficient programming. 💻✨

---

## 💡 Project Overview  

The goal is simple yet challenging: **rotate an `n x n` 2D matrix 90 degrees clockwise in place**. That means modifying the original matrix without creating a new one.

Here’s what you’ll achieve:
- 🧠 Understand 2D matrices in Python.
- 🔄 Perform in-place operations to optimize space.
- 🎯 Learn matrix transposition and row reversal techniques.

---

## 🔧 Getting Started  

### Prerequisites  
Before diving in, ensure you have the following:
- **Python 3.8.10** installed on Ubuntu 20.04 LTS.
- A text editor like `vim`, `vi`, or `emacs`.
- Familiarity with Python basics and matrix operations.

### Project Files  
- **`0-rotate_2d_matrix.py`**: Your implementation of the rotation algorithm.  
- **`main_0.py`**: Test file to validate your solution.  
- **`README.md`**: This file you're reading right now! 😄  

---

## 🚀 How to Implement  

1. **Matrix Representation**:  
   A matrix is represented as a list of lists in Python. For example:
   ```python
   matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
   ```

2. **Steps to Rotate**:
   - **Transpose** the matrix: Swap rows and columns.
   - **Reverse each row**: This creates the desired rotation.

3. **Prototype**:
   ```python
   def rotate_2d_matrix(matrix):
       """
       Rotate an n x n 2D matrix 90 degrees clockwise in place.
       """
       # Your implementation here
   ```

4. **Expected Output**:
   ```bash
   Input:
   [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

   Output:
   [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]
   ```

---

## 🛠️ Requirements  

### General:
- Use only built-in Python capabilities. **No imports allowed!** 📜
- Follow the **`pycodestyle` style guide (v2.8.0)**.
- Ensure all files are **executable** and include a shebang (`#!/usr/bin/python3`).
- Write **clear and concise documentation** for all modules and functions.

### Environment:
- **OS**: Ubuntu 20.04 LTS 🐧  
- **Python version**: 3.8.10 🐍

---

## 🧪 Testing  

Run the provided test script to validate your implementation:  
```bash
$ ./main_0.py
```

Expected output:  
```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

---

## 🌟 Key Concepts  

### 1. Matrix Transposition:  
Swapping rows and columns in the matrix:
```python
matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### 2. Reverse Rows:
Reverse each row for the final rotation:
```python
for row in matrix:
    row.reverse()
```

### 3. In-Place Operations:
Avoid creating a new matrix to save memory. Modify the original matrix directly. 🚀

---

## 📚 Resources  

- **Python Docs**:
  - [Lists in Python](https://docs.python.org/3/tutorial/datastructures.html)
- **GeeksforGeeks**:
  - [Inplace Rotate a Square Matrix](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- **TutorialsPoint**:
  - [Matrix Basics](https://www.tutorialspoint.com/python/python_lists.htm)

---

## 📂 Folder Structure  

```plaintext
📂 Rotate_2D_Matrix
├── 0-rotate_2d_matrix.py   # Algorithm implementation
├── main_0.py               # Test script
└── README.md               # Project documentation
```

---

**Happy Coding!** 🎉 
