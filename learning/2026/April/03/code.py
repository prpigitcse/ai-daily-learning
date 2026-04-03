"""
Code Explanation:
- `epochs = 10000`: An "epoch" in machine learning is one complete pass through the training cycle. We give the machine 10,000 attempts to find a better weight and bias.
- `random.uniform(-learning_rate, learning_rate)`: We generate a small random nudge. The `learning_rate` dictates the maximum size of the step our algorithm can take.
- `test_predictions = [...]` and `test_loss = ...`: We perform a **Forward Pass** using our temporary `test_weight` and `test_bias`, then immediately calculate the resulting Mean Squared Error.
- `if test_loss < best_loss:`: This is the core logic of our optimizer. If our random nudge resulted in a lower error than our previous best, we permanently save the new weight, bias, and loss. If the error went up, we ignore the test values and try a different random direction on the next loop iteration.
"""

import random

def mean_squared_error(actuals: list[float], predictions: list[float]) -> float:
    """Calculate the mean squared error between actual values and predictions."""
    if len(actuals) != len(predictions):
        raise ValueError("Actuals and predictions must have the same length.")
    
    squared_errors = [(a - p) ** 2 for a, p in zip(actuals, predictions)]
    return sum(squared_errors) / len(squared_errors)

# Dataset: Square footage (in thousands) -> House Price (in thousands)
# Example: 1.0 sqft -> $150, 2.0 sqft -> $250, 3.0 sqft -> $350
# The underlying pattern we want the AI to learn is: Price = (100 * sqft) + 50
X = [1.0, 2.0, 3.0] 
y_true = [150.0, 250.0, 350.0]

# Initial random guesses for weight (m) and bias (b)
best_weight = 0.0
best_bias = 0.0

# Calculate our initial starting error
initial_predictions = [(best_weight * x) + best_bias for x in X]
best_loss = mean_squared_error(y_true, initial_predictions)

epochs = 10000 # Number of times we will try to learn
learning_rate = 1.0 # How big of a random step we take

for epoch in range(epochs):
    # 1. Nudge the weights in a random direction
    test_weight = best_weight + random.uniform(-learning_rate, learning_rate)
    test_bias = best_bias + random.uniform(-learning_rate, learning_rate)

    # 2. Make new predictions with the nudged weights
    test_predictions = [(test_weight * x) + test_bias for x in X]
    
    # 3. Calculate the new error
    test_loss = mean_squared_error(y_true, test_predictions)

    # 4. If the error is lower, keep the new weights!
    if test_loss < best_loss:
        best_loss = test_loss
        best_weight = test_weight
        best_bias = test_bias

print(f"Best Weight = {best_weight:.2f}")
print(f"Best Bias   = {best_bias:.2f}")
print(f"Best Loss   = {best_loss:.2f}")