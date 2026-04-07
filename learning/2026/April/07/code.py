"""
Code Explanation:
- `def dot_vector(self, vector: list[float]) -> list[float]:` We define the method to multiply our Matrix by a 1D list.
- `if self.number_of_cols != len(vector):` The crucial dimensionality check. A $(m \times n)$ matrix can only multiply a vector of length $n$. 
- `sum(a * b for a, b in zip(row, vector))` This is the exact dot product logic. 
- `[ ... for row in self.data]` We wrap the dot product in a list comprehension, executing it for every single row in the matrix, returning a list of predictions.
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

    def __repr__(self) -> str:
        """Helper to print the matrix cleanly in the terminal."""
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix(\n  {rows_str}\n)"
    

# --- Example Usage: The Batch Forward Pass ---

# Design Matrix (X): 3 Houses, 2 Features (SqFt in thousands, Age)
X = Matrix([
    [2.0, 10.0],  # House 1
    [1.5, 5.0],   # House 2
    [3.0, 20.0]   # House 3
])

# Weights Vector (w): Importance of SqFt, Importance of Age
weights = [100.0, -2.0]

# Calculate predictions for ALL houses in one operation: Xw
batch_predictions = X.dot_vector(weights)

print("Design Matrix (X):")
print(X)
print(f"\nWeights (w): {weights}")
print(f"\nBatch Predictions (Xw): {batch_predictions}")
# Expected Output: [180.0, 140.0, 260.0]