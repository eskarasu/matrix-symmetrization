# matrix-symmetrization

This repository contains a Python script that utilizes NumPy to symmetrize a matrix. It takes a matrix with a filled upper triangle and completes the lower triangle to make it symmetric. This is useful for data analysis and machine learning tasks where symmetric matrices are required.

## Description

The script includes two main functionalities:
1. **Reflecting the lower left triangle to the upper right triangle**: This ensures that the matrix is symmetric by copying values from the lower triangle to the upper triangle.
2. **Filling missing values**: The script fills the missing values (None) in a matrix by copying corresponding values from the other side of the diagonal.

## Usage

### Prerequisites

- Python 3.x
- NumPy library

You can install NumPy using pip:

```bash
pip install numpy
```
## Script
```

import numpy as np

matrix_1 = np.array([
    [67.00, 19.00, 19.00, 19.00],
    [None, 67.00, 16.00, 16.00],
    [None, None, 67.00, 16.00],
    [None, None, None, 67.00]
])

# Get the size of the matrix
n = matrix_1.shape[0]

# Reflect the lower left triangle to the upper right triangle
for i in range(n):
    for j in range(i+1, n):
        matrix_1[j, i] = matrix_1[i, j]

print("Reflected matrix: " + str(matrix_1))

matrix_2 = np.array([
    [27, None, None, None],
    [8, 27, None, None],
    [8, 6, 27, None],
    [8, 6, 6, 27]
])

def fill_symmetric(matrix):
    """
    This function fills the missing values (None) in a matrix by copying
    corresponding values from the other side of the diagonal, making the
    matrix symmetric.

    Args:
        matrix: The input NumPy array (matrix).
    """
    for i in range(len(matrix)):  # Iterate over rows
        for j in range(len(matrix[i])):  # Iterate over columns
            if matrix[i][j] is None and matrix[j][i] is not None:
                matrix[i][j] = matrix[j][i]  # Copy value from the other side

fill_symmetric(matrix_2)
fill_symmetric(matrix_1)
print("Filled symmetric matrix 1: \n" + str(matrix_1) + "\n")
print("Filled symmetric matrix 2: \n" + str(matrix_2) + "\n")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

