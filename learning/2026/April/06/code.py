"""
Code Explanation:
- `def __validate(self, data)`: Extracted validation logic into a private method to keep the initialization clean.
- `def __mul__(self, scalar)`: Overloads the `*` operator. It uses a nested list comprehension to iterate through every row, and every element in that row, multiplying it by the scalar.
- `def __add__(self, other)`: Overloads the `+` operator. 
- `if self.shape != other.shape`: The mathematical safeguard guaranteeing we only add matrices of identical dimensions.
- `zip(self.data, other.data)`: A highly optimized Python technique to pair up corresponding rows, and then corresponding elements within those rows, to perform the addition.
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
            return NotImplemented

    def __repr__(self) -> str:
        """Helper to print the matrix cleanly in the terminal."""
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix(\n  {rows_str}\n)"


# --- Example Usage ---

dataset = Matrix([
    [2000.0, 3.0], # House 1: 2000 sqft, 3 beds
    [1500.0, 2.0], # House 2: 1500 sqft, 2 beds
])

# 1. Scalar Multiplication (Scaling down the data)
scaled_dataset = dataset * 0.1

print("Original Dataset:")
print(dataset)
print("\nScaled Dataset (multiplied by 0.1):")
print(scaled_dataset)

# 2. Matrix Addition (Shifting data)
shift_matrix = Matrix([
    [10.0, 10.0], 
    [10.0, 10.0]
])

shifted_dataset = dataset + shift_matrix

print("\nShifted Dataset (+ 10 to all elements):")
print(shifted_dataset)