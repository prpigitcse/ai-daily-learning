"""
Code Explanation:
- `class SimpleLinearRegressor`: We define our model as a standalone object. It owns its own parameters (weight, bias) and hyperparameters (learning_rate, epochs).
- `def fit(self, X, y)`: The training engine. We moved our brute-force optimization loop entirely inside this method. The model iterates through epochs, adjusts `self.weight` and `self.bias`, and saves the state that results in the lowest Mean Squared Error.
- `def predict(self, X)`: The inference engine. Once `.fit()` has found the optimal parameters, `.predict()` uses those saved parameters to calculate $\hat{y} = wx + b$ on entirely new data.
- `model.fit(X_train, y_train)` followed by `model.predict(X_test)`: This is the exact, universal API sequence used by professional data scientists across almost all Python ML frameworks.
"""

import random

def mean_squared_error(actuals: list[float], predictions: list[float]) -> float:
    """Calculate the mean squared error between actual values and predictions."""
    if len(actuals) != len(predictions):
        raise ValueError("Actuals and predictions must have the same length.")
    
    squared_errors = [(a - p) ** 2 for a, p in zip(actuals, predictions)]
    return sum(squared_errors) / len(squared_errors)

class SimpleLinearRegressor:
    def __init__(self, learning_rate: float = 1.0, epochs: int = 10000):
        # Hyperparameters (settings for how the model learns)
        self.learning_rate = learning_rate
        self.epochs = epochs
        
        # Parameters (what the model actually learns)
        self.weight = 0.0
        self.bias = 0.0
        self.best_loss = float('inf')

    def fit(self, X: list[float], y: list[float]) -> None:
        """Trains the model by optimizing weight and bias to minimize MSE."""
        for epoch in range(self.epochs):
            # 1. Nudge the weights in a random direction
            test_weight = self.weight + random.uniform(-self.learning_rate, self.learning_rate)
            test_bias = self.bias + random.uniform(-self.learning_rate, self.learning_rate)

            # 2. Make new predictions with the nudged weights
            test_predictions = [(test_weight * x) + test_bias for x in X]
            
            # 3. Calculate the new error
            test_loss = mean_squared_error(y, test_predictions)

            # 4. If the error is lower, keep the new weights!
            if test_loss < self.best_loss:
                self.best_loss = test_loss
                self.weight = test_weight
                self.bias = test_bias

    def predict(self, X: list[float]) -> list[float]:
        """Generates predictions using the trained weight and bias."""
        return [(self.weight * x) + self.bias for x in X]

# --- The Scikit-Learn Style API in Action ---

# 1. Instantiate the model
model = SimpleLinearRegressor(learning_rate=1.0, epochs=10000)

# 2. Train the model on known data
X_train = [1.0, 2.0, 3.0]
y_train = [150.0, 250.0, 350.0]
model.fit(X_train, y_train)

# 3. Predict on NEW, unseen data
X_test = [4.0, 5.0]
predictions = model.predict(X_test)

print(f"Trained Weight: {model.weight:.2f}")
print(f"Trained Bias:   {model.bias:.2f}")
print(f"Predictions for 4.0 and 5.0 sqft: {[f'{p:.2f}' for p in predictions]}")