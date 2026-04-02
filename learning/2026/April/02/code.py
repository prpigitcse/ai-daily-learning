"""
Code Explanation:
- `def mean_squared_error(actuals: list[float], predictions: list[float]) -> float`: A standalone function that takes two lists of numbers representing the ground truth ($y$) and our model's outputs ($\hat{y}$).
- `if len(actuals) != len(predictions):`: We first check if the two lists have the same length. If not, we raise a `ValueError` because we cannot compare values that don't correspond to each other.
- `squared_errors = [(a - p) ** 2 for a, p in zip(actuals, predictions)]`: This is a list comprehension that iterates through both lists simultaneously using `zip`. For each pair of actual and predicted values, it calculates the difference, squares it, and adds it to the `squared_errors` list.
- `return sum(squared_errors) / len(squared_errors)`: Finally, we calculate the mean by summing up all the squared errors and dividing by the total number of values. This gives us the average squared difference between our predictions and the actual values.
"""

def mean_squared_error(actuals: list[float], predictions: list[float]) -> float:
    """Calculate the mean squared error between actual values and predictions."""
    if len(actuals) != len(predictions):
        raise ValueError("Actuals and predictions must have the same length.")
    
    squared_errors = [(a - p) ** 2 for a, p in zip(actuals, predictions)]
    return sum(squared_errors) / len(squared_errors)

# Example Usage: Evaluating our model on a dataset of 3 houses

# 1. Ground Truth (Actual selling prices in thousands)
actual_prices = [300.0, 450.0, 200.0]

# 2. Our Model's Guesses (Predictions in thousands based on weights/bias)
predicted_prices = [310.0, 430.0, 250.0]

# 3. Calculate how wrong the model was overall
mse_loss = mean_squared_error(actual_prices, predicted_prices)

print(f"Actual Prices:    {actual_prices}")
print(f"Predicted Prices: {predicted_prices}")
print(f"Mean Squared Error: {mse_loss:.2f}")

# Note: An MSE of 1000.0 means the average squared error is 1000. 
# To get the error back into the original units (thousands of dollars), 
# we would take the square root of the MSE (Root Mean Squared Error).