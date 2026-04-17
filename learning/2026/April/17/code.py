"""
Code Explanation:
This is the culmination of three weeks of from-scratch development. 
- The `Matrix` class handles the linear algebra.
- `_fit_transform` computes the Z-score statistics (mu, sigma) and saves them to the object's state.
- `_transform` strictly uses the saved statistics, preventing data leakage during prediction.
- The `fit` loop executes the batch gradient descent calculus exactly as derived.
"""
import math
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
    
    def copy(self) -> "Matrix":
        """Returns a deep copy of the matrix."""
        return Matrix([row[:] for row in self.data])

    @property
    def T(self) -> "Matrix":
        """Returns the transpose of the matrix."""
        return Matrix([[self.data[i][j] for i in range(self.number_of_rows)] for j in range(self.number_of_cols)])
    def __repr__(self) -> str:
        """Helper to print the matrix cleanly in the terminal."""
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix(\n  {rows_str}\n)"
class LinearRegressor:
    def __init__(self, learning_rate: float = 0.01, epochs: int = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0
        
        # Use None for proper fitted-state tracking
        self.feature_means = []
        self.feature_stds = []

    def _check_is_fitted(self):
        if self.feature_means is None or self.feature_stds is None:
            raise ValueError("Scaler has not been fitted yet. Call fit first.")

    def _fit_scaler(self, X: "Matrix") -> None:
        """Compute mean and std from training data."""
        
        columns = list(zip(*X.data))
        
        self.feature_means = [sum(col) / len(col) for col in columns]
        
        self.feature_stds = [
            math.sqrt(sum((x - mean) ** 2 for x in col) / len(col))
            for col, mean in zip(columns, self.feature_means)
        ]

    def __get_scaled_matrix(self, X: "Matrix") -> "Matrix":
        """Apply scaling using already computed stats."""
        
        self._check_is_fitted()
        
        scaled_data = []
        
        for row in X.data:
            if len(row) != len(self.feature_means):
                raise ValueError("Feature size mismatch during transform.")
            
            scaled_row = [
                (x - mean) / std if std > 0 else 0.0
                for x, mean, std in zip(row, self.feature_means, self.feature_stds)
            ]
            scaled_data.append(scaled_row)
        
        return Matrix(scaled_data)

    def _transform(self, X: "Matrix") -> "Matrix":
        """Transform data using fitted scaler."""
        return self.__get_scaled_matrix(X)

    def _fit_transform(self, X: "Matrix") -> "Matrix":
        """Fit scaler and transform in one step (training path)."""
        self._fit_scaler(X)
        return self._transform(X)

    def forward_pass(self, X: "Matrix", w: list[float], b: float) -> list[float]:
        """Batch prediction: Xw + b"""
        return [p + b for p in X.dot_vector(w)]
    
    def calculate_mse(self, y: list[float], y_hat: list[float]) -> float:
        """Mean Squared Error for the batch."""
        N = len(y)
        return (1 / N) * sum((p - a) ** 2 for p, a in zip(y_hat, y))
    
    def get_batch_gradients(
        self, 
        X: "Matrix", 
        y: list[float], 
        y_hat: list[float]
    ) -> tuple[list[float], float]:
        """
        Calculates gradients for weights and bias.
        Returns: (w_gradients, b_gradient)
        """
        N = len(y)
        
        # Error vector: (y_hat - y)
        error_vector = [p - a for p, a in zip(y_hat, y)]
        
        # Bias gradient
        b_gradient = (2 / N) * sum(error_vector)
        
        # Weight gradients: (2/N) * X^T * error_vector
        w_gradients = [
            (2 / N) * g for g in X.T.dot_vector(error_vector)
        ]

        return w_gradients, b_gradient
    
    def fit(self, X: "Matrix", y: list[float]) -> None:
        """Trains the model using batch gradient descent."""
        X_scaled = self._fit_transform(X)
        
        # Initialize weights and bias
        self.weights = [0.0] * X_scaled.number_of_cols
        self.bias = 0.0
        
        for _ in range(self.epochs):
            y_hat = self.forward_pass(X_scaled, self.weights, self.bias)
            w_gradients, b_gradient = self.get_batch_gradients(X_scaled, y, y_hat)
            
            # Update weights and bias
            self.weights = [w - self.learning_rate * gw for w, gw in zip(self.weights, w_gradients)]
            self.bias -= self.learning_rate * b_gradient

    def predict(self, X: "Matrix") -> list[float]:
        """Predicts using the trained model."""
        X_scaled = self._transform(X)
        return self.forward_pass(X_scaled, self.weights, self.bias)
    

# --- Test ---
X_train = Matrix([
    [1000.0, 10.0],
    [2000.0, 5.0],
    [3000.0, 20.0]
])
y_train = [130.0, 240.0, 310.0]

model = LinearRegressor(learning_rate=0.1, epochs=100)
model.fit(X_train, y_train)

# Test on a new, unseen house (2500 SqFt, 2 years old)
X_test = Matrix([[2500.0, 2.0]])
predictions = model.predict(X_test)

print(f"Final Weights: {model.weights}")
print(f"Final Bias: {model.bias}")
print(f"Prediction for 2500 SqFt, 2 yrs old: {predictions}")