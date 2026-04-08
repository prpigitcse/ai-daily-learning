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
    