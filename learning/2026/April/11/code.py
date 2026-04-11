"""
Code Explanation:
- `self.weights = []`: We initialize weights as an empty list because the model does not know how many features the dataset has until `.fit()` is called.
- `if not self.weights:`: Dynamic initialization. We look at `X.shape` (the number of columns) and create a starting weight of 0.0 for every single feature.
- `test_weights = [...]`: Because we have multiple weights, we must nudge each one individually using a list comprehension.
- `[p + test_bias for p in X.dot_vector(test_weights)]`: The Batch Forward Pass! We multiply the entire dataset by our weights, and then add our single scalar bias to every resulting prediction.
"""
import random
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

def mean_squared_error(actuals: list[float], predictions: list[float]) -> float:
    return sum((a - p) ** 2 for a, p in zip(actuals, predictions)) / len(actuals)

class BatchLinearRegressor:
    def __init__(self, learning_rate: float = 1.0, epochs: int = 10000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        
        # We start with empty weights because we don't know how many features X has yet!
        self.weights = [] 
        self.bias = 0.0
        self.best_loss = float('inf')

    def fit(self, X: Matrix, y: list[float]) -> None:
        # 1. Initialize self.weights with 0.0 for every column in X
        if not self.weights:
            self.weights = [0.0 for _ in range(X.shape[1])]

        for epoch in range(self.epochs):
            test_weights = [weight + random.uniform(-self.learning_rate, self.learning_rate) for weight in self.weights]
            test_bias = self.bias + random.uniform(-self.learning_rate, self.learning_rate)
            test_predictions = [p + test_bias for p in X.dot_vector(test_weights)]
            test_loss = mean_squared_error(y, test_predictions)

            # 4. If the error is lower, keep the new weights!
            if test_loss < self.best_loss:
                self.best_loss = test_loss
                self.weights = test_weights
                self.bias = test_bias

    def predict(self, X: Matrix) -> list[float]:
        """Generates predictions for new batch data."""
        return [p + self.bias for p in X.dot_vector(self.weights)] 


# --- Example Usage: The Capstone Test ---

# Dataset: 2 Features (SqFt in thousands, Age in years) -> Price (in thousands)
# True pattern: Price = (100 * SqFt) + (-2 * Age) + 50
X_train = Matrix([
    [1.0, 10.0],
    [2.0, 5.0],
    [3.0, 20.0]
])
y_train = [130.0, 240.0, 310.0]

# Train the engine
model = BatchLinearRegressor(learning_rate=1.0, epochs=20000)
model.fit(X_train, y_train)

# Test on completely unseen data: A 4000 SqFt house that is 2 years old
X_test = Matrix([[4.0, 2.0]]) 

print(f"Trained Weights: {[round(w, 2) for w in model.weights]}")
print(f"Trained Bias: {model.bias:.2f}")
print(f"Prediction for 4000 SqFt, 2 yrs old: {[round(p, 2) for p in model.predict(X_test)]}")