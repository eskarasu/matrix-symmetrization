import numpy as np

matrix_1 = np.array([
    [67.00, 19.00, 19.00, 19.00, 19.00, 19.00, 24.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 53.00, 53.00, 67.00, 67.00],
    [None, 67.00, 16.00, 16.00, 16.00, 19.00, 19.00, 24.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 53.00, 53.00, 67.00, 67.00],
    [None, None, 67.00, 16.00, 16.00, 19.00, 19.00, 24.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 53.00, 53.00, 67.00, 67.00],
    [None, None, None, 67.00, 16.00, 19.00, 19.00, 24.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 53.00, 53.00, 67.00, 67.00],
    [None, None, None, None, 67.00, 19.00, 19.00, 24.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 53.00, 53.00, 67.00, 67.00],
    [None, None, None, None, None, 67.00, 24.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 53.00, 53.00, 67.00, 67.00],
    [None, None, None, None, None, None, 67.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 29.00, 53.00, 53.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, 53.00, 53.00, 53.00, 53.00, 53.00, 53.00, 53.00, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, 53.00, 53.00, 53.00, 53.00, 53.00, 53.00, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, 53.00, 53.00, 53.00, 53.00, 53.00, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, 53.00, 53.00, 53.00, 53.00, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, None, 53.00, 53.00, 53.00, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, None, None, 53.00, 53.00, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, 53.00, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 67.00, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 67.00, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 67.00, 67.00],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 67.00],
])

# Get the size of the matrix
n = matrix_1.shape[0]

# Reflect the lower left triangle to the upper right triangle
for i in range(n):
    for j in range(i+1, n):
        matrix_1[j, i] = matrix_1[i, j]

print("Reflected matrix: " + str(matrix_1))

matrix_2 = np.array([
        [27, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [8, 27, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [8, 6, 27, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [8, 6, 6, 27, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [8, 6, 6, 6, 27, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [8, 8, 8, 8, 8, 27, None, None, None, None, None, None, None, None, None, None, None, None],
        [8, 8, 8, 8, 8, 6, 27, None, None, None, None, None, None, None, None, None, None, None],
        [13, 8, 8, 8, 8, 6, 6, 21, None, None, None, None, None, None, None, None, None, None],
        [13, 13, 13, 13, 8, 8, 6, 6, 21, None, None, None, None, None, None, None, None, None],
        [13, 13, 13, 13, 13, 8, 8, 6, 6, 21, None, None, None, None, None, None, None, None],
        [13, 13, 13, 13, 13, 8, 8, 6, 6, 0, 21, None, None, None, None, None, None, None],
        [13, 13, 13, 13, 13, 13, 13, 13, 6, 6, 6, 21, None, None, None, None, None, None],
        [13, 13, 13, 13, 13, 13, 8, 8, 13, 13, 13, 6, 18, None, None, None, None, None],
        [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 6, 13, None, None, None, None],
        [21, 21, 21, 21, 18, 18, 18, 13, 13, 13, 13, 13, 8, 6, 21, None, None, None],
        [21, 21, 21, 21, 21, 21, 21, 18, 18, 18, 18, 13, 13, 8, 6, 21, None, None],
        [27, 27, 27, 27, 21, 21, 21, 21, 21, 21, 21, 18, 13, 13, 8, 6, 27, None],
        [27, 27, 27, 27, 27, 27, 27, 21, 21, 21, 21, 21, 18, 13, 13, 8, 6, 27]
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
print("filled symetric matrix: \n \n" + str(matrix_1) + "\n")
print("filled symetric matrix: \n \n" + str(matrix_2) + "\n")
