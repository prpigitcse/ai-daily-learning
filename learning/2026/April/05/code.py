"""
Code Explanation:
- `class Matrix:` We define our foundational 2D data structure.
- `def __init__(self, data: list[list[float]]):` The matrix is initialized with a list of lists.
- `if len(row) != self.number_of_cols:` This is a critical validation check. A mathematical matrix must be a perfect rectangle. If one row has 3 features and another has 4, the math will crash.
- `@property def shape(self):` In ML libraries like NumPy, `.shape` returns the dimensions `(rows, columns)`. We use the `@property` decorator so it can be accessed like an attribute (`X.shape`) rather than a method (`X.shape()`).
"""

class Matrix:
    def __init__(self, data: list[list[float]]):
        self.data = data
        if data:
            self.number_of_rows = len(data)
            self.number_of_cols = len(data[0])
            
            # Validation: Ensure all rows have the exact same number of columns
            for row in data:
                if len(row) != self.number_of_cols:
                    raise ValueError("All rows must have the same number of columns to form a valid matrix.")
        else:
            self.number_of_rows = 0
            self.number_of_cols = 0

    @property
    def shape(self) -> tuple[int, int]:
        """Returns the shape of the matrix as (rows, columns)."""
        return (self.number_of_rows, self.number_of_cols)

    def __repr__(self) -> str:
        """Helper to print the matrix cleanly in the terminal."""
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix(\n  {rows_str}\n)"


# Example Usage: Creating a Design Matrix for 3 houses

house_dataset = [
    [3.0, 2.0, 15.0, 2000.0], # House 1
    [4.0, 3.0, 10.0, 2500.0], # House 2
    [2.0, 1.0, 50.0, 1200.0]  # House 3
]

X = Matrix(house_dataset)

print("Design Matrix X:")
print(X)
print(f"\nThe shape of X is: {X.shape}")
print(f"Number of samples (houses): {X.shape}")
print(f"Number of features: {X.shape[1]}")