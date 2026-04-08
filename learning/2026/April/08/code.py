"""
Code Explanation:
- `def dot_matrix(self, other: "Matrix") -> "Matrix":` We define the method to multiply our Matrix by another Matrix.
- `if self.number_of_cols != other.number_of_rows:` The ultimate dimensionality check. A matrix of shape $(m, n)$ can only be multiplied by a matrix of shape $(n, p)$.
- `sum(self.data[i][k] * other.data[k][j] ...)`: This is the exact translation of the mathematical summation $C_{ij} = \sum A_{ik} B_{kj}$. It computes the dot product of row `i` from the first matrix and column `j` from the second matrix.
- `for j in range(...)` and `for i in range(...)`: The outer loops build the new matrix $C$, ensuring its final shape is $(m, p)$.
"""
class Matrix:
    def __init__(self, data: list[list[float]]):
        if data:
            self.__validate(data)
            self.data = data
            self.number_of_rows = len(data)
            self.number_of_cols = len(data[0])            
        else:
            self.data = []
            self.number_of_rows = 0
            self.number_of_cols = 0

    def __validate(self, data: list[list[float]]) -> None:
        """Private method to ensure matrix is a perfect rectangle."""
        number_of_cols = len(data[0])
        for row in data:
            if len(row) != number_of_cols:
                raise ValueError("All rows must have the same number of columns to form a valid matrix.")

    @property
    def shape(self) -> tuple[int, int]:
        """Returns the shape of the matrix as (rows, columns)."""
        return (self.number_of_rows, self.number_of_cols)
    
    def __mul__(self, scalar: float) -> "Matrix":
        """Scalar multiplication: scales every element by the scalar."""
        return Matrix([[element * scalar for element in row] for row in self.data])

    def __add__(self, other: "Matrix") -> "Matrix":
        """Matrix addition: adds elements of identically shaped matrices."""
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices must have the same shape for addition")
            return Matrix([
                [a + b for a, b in zip(row1, row2)]
                for row1, row2 in zip(self.data, other.data)
            ])
        else:
            raise TypeError(f"Unsupported operand type for +: 'Matrix' and '{type(other).__name__}'")
        
    def dot_vector(self, vector: list[float]) -> list[float]:
        """Multiplies the matrix by a 1D vector (Batch Dot Product)."""
        if self.number_of_cols != len(vector):
            raise ValueError("The number of columns in the matrix must exactly equal the number of elements in the vector")
        return [sum(a * b for a, b in zip(row, vector)) for row in self.data]
    
    def dot_matrix(self, other: "Matrix") -> "Matrix":
        """Multiplies the matrix by another matrix (Batch Matrix Multiplication)."""
        if self.number_of_cols != other.number_of_rows:
            raise ValueError("The number of columns in the first matrix must equal the number of rows in the second matrix for multiplication")
        
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(other.number_of_rows))
                for j in range(other.number_of_cols)
            ]
            for i in range(self.number_of_rows)
        ]
        
        return Matrix(result)

    def __repr__(self) -> str:
        """Helper to print the matrix cleanly in the terminal."""
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix(\n  {rows_str}\n)"
    
    
# --- Example Usage: Pushing Data through a Hidden Layer ---

# Dataset X: 2 Houses, 4 Features (Beds, Baths, Age, SqFt)
X = Matrix([
    [3.0, 2.0, 15.0, 2000.0],
    [4.0, 3.0, 10.0, 2500.0]
])

# Weight Matrix W1: Maps 4 input features to 2 hidden concepts ("Size Score", "Modernity Score")
# Shape must be (4, 2) so inner dimensions match X's (2, 4)
W1 = Matrix([
    [10.0, 0.0],   # Weights for Beds
    [5.0,  0.0],   # Weights for Baths
    [0.0, -2.0],   # Weights for Age
    [1.0,  0.0]    # Weights for SqFt
])

# Forward pass through the hidden layer: X * W1
hidden_layer_output = X.dot_matrix(W1)

print(f"Dataset Shape: {X.shape}")
print(f"Weights Shape: {W1.shape}")
print("\nHidden Layer Output (New Transformed Dataset):")
print(hidden_layer_output)
print(f"Output Shape: {hidden_layer_output.shape}")