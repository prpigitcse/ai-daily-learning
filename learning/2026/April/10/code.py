"""
Code Explanation:
- `def get_column(self, index: int) -> list[float]:` A utility method to extract a feature column for analysis.
- `if index < 0 or index >= self.number_of_cols:` A boundary check to ensure we don't try to access a column that doesn't exist.
- `[row[index] for row in self.data]`: A clean list comprehension that iterates through every row and extracts the specific element at the requested index.
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
    
    def get_column(self, index: int) -> list[float]:
        """Returns a specific column from the matrix as a 1D list."""
        if not 0 <= index < self.number_of_cols:
            raise IndexError("Column index is out of bounds")
        return [row[index] for row in self.data]

    @property
    def T(self) -> "Matrix":
        """Returns the transpose of the matrix."""
        return Matrix([[self.data[i][j] for i in range(self.number_of_rows)] for j in range(self.number_of_cols)])
    def __repr__(self) -> str:
        """Helper to print the matrix cleanly in the terminal."""
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix(\n  {rows_str}\n)"

# A dataset with 3 features: [Beds, SqFt, SqMeters]
# Notice that SqFt and SqMeters measure the exact same thing (1 SqM ~ 10.76 SqFt)
X = Matrix([
    [3.0, 1000.0, 92.9],
    [4.0, 2000.0, 185.8],
    [2.0, 1500.0, 139.4]
])

sqft_col = X.get_column(1)
sqm_col = X.get_column(2)

print(f"Square Footage Column: {sqft_col}")
print(f"Square Meters Column:  {sqm_col}")

# A simple check to see if they are perfectly correlated (linearly dependent)
ratios = [sqft / sqm for sqft, sqm in zip(sqft_col, sqm_col)]
print(f"\nRatio of SqFt to SqMeters for each row: {[f'{r:.2f}' for r in ratios]}")
print("Because the ratio is a constant (~10.76), these columns are linearly dependent!")
print("We should drop one of these columns before training an AI.")