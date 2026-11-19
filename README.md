# 3x3 Matrix Operations (GUI)

This project contains two separate Tkinter desktop applications:

1. **Without NumPy** — calculations use Python lists, loops, and formulas.
2. **With NumPy** — calculations use NumPy array operations.

## Features

- Matrix addition: A + B
- Matrix subtraction: A - B
- Matrix multiplication: A × B (standard row-by-column multiplication)
- Transpose of A
- Determinant of A
- Inverse of A (only when determinant is non-zero)
- Input validation and error messages
- Clear all input fields

Both matrices are 3 by 3. The input boxes start with identity matrices as examples; replace the values as needed.

## Requirements

- Python 3.9 or later
- Tkinter (included with most standard Windows Python installations)
- NumPy is required only for the NumPy version

## Run on Windows

Open Command Prompt in the project folder.

### Version 1: Without NumPy

```bat
cd without_numpy
python matrix_gui.py
```

No third-party package is required.

### Version 2: With NumPy

```bat
py -m pip install numpy
cd ..\with_numpy
python matrix_gui.py
```

If `python` is not recognized, try `py` instead.

## Example matrices

Matrix A:
```text
1 2 3
4 5 6
7 8 9
```

Matrix B:
```text
9 8 7
6 5 4
3 2 1
```

For multiplication, the program uses standard matrix multiplication, not cell-by-cell multiplication.

## Project structure

```text
Matrix_Operations_GUI/
├── README.md
├── without_numpy/
│   └── matrix_gui.py
└── with_numpy/
    ├── matrix_gui.py
    └── requirements.txt
```

## Learning concepts

- Tkinter GUI: Window, labels, frames, buttons, and text area
- Functions and classes
- Python lists and nested loops
- NumPy arrays and `numpy.linalg`
- Exception handling and input validation
- Matrix arithmetic and 3x3 determinant/inverse
