"""
Code Explanation:
This encapsulates the Regularized Regressor class. It prevents data leakage via Z-score state management and applies the mathematically scaled penalty (divided by N) directly into the gradient descent loop.
"""

import csv
import math
from pathlib import Path
from typing import Literal, overload
import numpy as np
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
class LinearRegression:
    def __init__(self, learning_rate: float = 0.01, epochs: int = 1000, lambda_param: float = 1.0, type: str = "linear"):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.lambda_param = lambda_param
        self.type = type
        self.weights = []
        self.bias = 0.0
        
        # Use None for proper fitted-state tracking
        self.feature_means = []
        self.feature_stds = []

    def _check_is_fitted(self):
        if not self.feature_means or not self.feature_stds:
            raise ValueError("Scaler has not been fitted yet. Call fit first.")

    def _fit_scaler(self, X: "Matrix") -> None:
        """Compute mean and std from training data."""
        if not X.data:
            raise ValueError("Training data cannot be empty.")
        
        columns = list(zip(*X.data))
        
        self.feature_means = np.mean(columns, axis=1).tolist()
        
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
    
    def get_batch_base_gradients(
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
        w_gradients_base = [
            (2 / N) * g for g in X.T.dot_vector(error_vector)
        ]

        return w_gradients_base, b_gradient
    
    def get_batch_penalty_gradients_ridge(self, w: list[float], n: int) -> list[float]:
        """Calculates L2 penalty gradients for weights."""
        return [(2 * (self.lambda_param / n) * weight) for weight in w]
    
    def get_batch_penalty_gradients_lasso(self, w: list[float], n: int) -> list[float]:
        """Calculates L1 penalty gradients for weights."""
        return [(self.lambda_param / n) * (1 if weight > 0 else -1 if weight < 0 else 0) for weight in w]
    
    def get_batch_penalty_gradients_elasticnet(self, w: list[float], n: int) -> list[float]:
        """Calculates combined L1 and L2 penalty gradients for weights."""
        l1_gradients = self.get_batch_penalty_gradients_lasso(w, n)
        l2_gradients = self.get_batch_penalty_gradients_ridge(w, n)
        return [l1 + l2 for l1, l2 in zip(l1_gradients, l2_gradients)]

    def fit(self, X: "Matrix", y: list[float]) -> None:
        """Trains the model using batch gradient descent."""
        X_scaled = self._fit_transform(X)
        
        # Initialize weights and bias
        self.weights = [0.0] * X_scaled.number_of_cols
        self.bias = 0.0
        
        for _ in range(self.epochs):
            y_hat = self.forward_pass(X_scaled, self.weights, self.bias)
            w_gradients_base, b_gradient = self.get_batch_base_gradients(X_scaled, y, y_hat)

            if self.type == "ridge":
                w_gradients_final = [w_grad + ridge_grad for w_grad, ridge_grad in zip(w_gradients_base, self.get_batch_penalty_gradients_ridge(self.weights, len(y)))]
            elif self.type == "lasso":
                w_gradients_final = [w_grad + lasso_grad for w_grad, lasso_grad in zip(w_gradients_base, self.get_batch_penalty_gradients_lasso(self.weights, len(y)))]
            elif self.type == "elasticnet":
                w_gradients_final = [w_grad + enet_grad for w_grad, enet_grad in zip(w_gradients_base, self.get_batch_penalty_gradients_elasticnet(self.weights, len(y)))]
            else:
                w_gradients_final = w_gradients_base

            # Update weights and bias
            self.weights = [w - self.learning_rate * gw for w, gw in zip(self.weights, w_gradients_final)]
            self.bias -= self.learning_rate * b_gradient

    def predict(self, X: "Matrix") -> list[float]:
        """Predicts using the trained model."""
        X_scaled = self._transform(X)
        return self.forward_pass(X_scaled, self.weights, self.bias)

def calculate_r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculates the R-squared metric.
    """
    if y_true.size == 0 or y_pred.size == 0:
        raise ValueError("R-squared requires non-empty true and predicted values.")
    if y_true.shape != y_pred.shape:
        raise ValueError("True and predicted values must have the same shape.")

    y_true_mean = np.mean(y_true)
    tss = np.sum((y_true - y_true_mean) ** 2)
    rss = np.sum((y_true - y_pred) ** 2)
    r2 = 1 - (rss / tss) if tss != 0 else 0
    return r2


def load_feature_names(csv_path: Path, target_column: str = "EnergyConsumption") -> list[str]:
    """Loads feature names in the same order used by load_training_data."""
    with csv_path.open(newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError(f"{csv_path} is missing header columns.")
        if target_column not in reader.fieldnames:
            raise ValueError(f"{target_column} column is missing from {csv_path}.")

        return [column for column in reader.fieldnames if column != target_column]


def format_feature_weights(feature_names: list[str], weights: list[float]) -> str:
    """Formats model weights as Feature: weight."""
    if len(feature_names) != len(weights):
        raise ValueError("Feature names and model weights must have the same length.")

    return ", ".join(
        f"{feature_name}: {weight:.6f}"
        for feature_name, weight in zip(feature_names, weights)
    )


@overload
def load_training_data(
    csv_path: Path,
    target_column: str = "EnergyConsumption",
    *,
    return_test_split: Literal[False] = False,
) -> tuple[Matrix, list[float]]: ...


@overload
def load_training_data(
    csv_path: Path,
    target_column: str = "EnergyConsumption",
    *,
    return_test_split: Literal[True],
) -> tuple[Matrix, list[float], Matrix, list[float]]: ...


def load_training_data(
    csv_path: Path,
    target_column: str = "EnergyConsumption",
    *,
    return_test_split: bool = False,
) -> tuple[Matrix, list[float]] | tuple[Matrix, list[float], Matrix, list[float]]:
    """Loads a CSV, splits it 80/20, and optionally returns both train and test sets."""
    with csv_path.open(newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError(f"{csv_path} is missing header columns.")
        if target_column not in reader.fieldnames:
            raise ValueError(f"{target_column} column is missing from {csv_path}.")

        feature_columns = [column for column in reader.fieldnames if column != target_column]
        features = []
        targets = []

        for row in reader:
            features.append([float(row[column]) for column in feature_columns])
            targets.append(float(row[target_column]))

    total_rows = len(features)
    if total_rows == 0:
        raise ValueError(f"{csv_path} does not contain any data rows.")
    if return_test_split and total_rows < 2:
        raise ValueError("At least 2 rows are required to create separate train and test splits.")

    if total_rows < 2:
        split_index = total_rows
    else:
        split_index = int(total_rows * 0.8)
        split_index = min(max(split_index, 1), total_rows - 1)

    X_train = Matrix(features[:split_index])
    y_train = targets[:split_index]
    X_test = Matrix(features[split_index:])
    y_test = targets[split_index:]

    if return_test_split:
        return X_train, y_train, X_test, y_test

    return X_train, y_train

# --- Test ---
base_dir = Path(__file__).resolve().parent.parent
engineered_dataset_path = base_dir / "23" / "engineered-dataset.csv"
raw_dataset_path = base_dir / "23" / "raw-dataset.csv"

# 1. Featured Engineered Data
X_train, y_train, X_test, y_test = load_training_data(engineered_dataset_path, return_test_split=True)

# 2. Raw Data
raw_X_train, raw_y_train, raw_X_test, raw_y_test = load_training_data(raw_dataset_path, return_test_split=True)

datasets = [engineered_dataset_path, raw_dataset_path]
lambda_values = [0.01, 0.1, 1, 10, 100]
regression_types = ["linear", "ridge", "lasso", "elasticnet"]

for dataset in datasets:
    for lambda_param in lambda_values:
        for reg_type in regression_types:
            print(f"Training {reg_type} regression on {dataset.name} with lambda={lambda_param}")
            model = LinearRegression(learning_rate=0.1, epochs=100, lambda_param=lambda_param, type=reg_type)
            feature_names = load_feature_names(dataset)
            X_train, y_train, X_test, y_test = load_training_data(dataset, return_test_split=True)
            model.fit(X_train, y_train)
            print(f"Model Weights: {format_feature_weights(feature_names, model.weights)}")
            print(f"Model Bias: {model.bias}")
            predictions = model.predict(X_test)
            r2_score = calculate_r2(np.array(y_test), np.array(predictions))
            print(f"{reg_type.capitalize()} Regression R^2 Score: {r2_score:.6f}\n")
