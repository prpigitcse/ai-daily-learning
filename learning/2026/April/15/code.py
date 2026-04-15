"""
Code Explanation:
- `X.T.dot_vector(error_vector)`: This single line replaces complex nested loops. It maps the error of every single prediction back to the specific features that caused it.
- `[w - learning_rate * w_gradient...]`: We update all the weights in par
allel using a list comprehension.
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


def forward_pass(X: "Matrix", w: list[float], b: float) -> list[float]:
    """Batch prediction: Xw + b"""
    return [p + b for p in X.dot_vector(w)]

def calculate_mse(y: list[float], y_hat: list[float]) -> float:
    """Mean Squared Error for the batch."""
    N = len(y)
    return (1/N) * sum([(p - a) ** 2 for p, a in zip(y_hat, y)])

def get_batch_gradients(X: "Matrix", y: list[float], y_hat: list[float]) -> tuple[list[float], float]:
    """
    Calculates the gradients for w and b using matrix calculus.
    Returns: (w_gradients_list, b_gradient_float)
    """
    N = len(y)
    
    # raw error vector: (y_hat - y)
    error_vector = [p - a for p, a in zip(y_hat, y)]
    
    # bias gradient: (2/N) * sum(error_vector)
    b_gradient = (2/N) * sum(error_vector)
    
    # weights gradient: (2/N) * X^T * error_vector
    w_gradients =  [(2/N) * gradient for gradient in X.T.dot_vector(error_vector)]
    
    return w_gradients, b_gradient

# Dataset: [SqFt (in thousands), Age] -> Price
X_train = Matrix([
    [1.0, 10.0],
    [2.0, 5.0],
    [3.0, 20.0]
])
y_train = [130.0, 240.0, 310.0]

# Initial parameters
w = [1.0, 1.0]
b = 1.0
learning_rate = 0.001
epochs = 15000

for epoch in range(epochs):
    y_hat = forward_pass(X_train, w, b)
    loss = calculate_mse(y_train, y_hat)
    w_gradients, b_gradient = get_batch_gradients(X_train, y_train, y_hat)
    w = [w - learning_rate * w_gradient for w, w_gradient in zip(w, w_gradients)]
    b = b - learning_rate * b_gradient
    print(f"Epoch {epoch + 1}: Weight = {w}, Bias = {b}, Loss = {loss}")