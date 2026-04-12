"""
Code Explanation:
- `def get_gradient(w: float) -> float:` This function represents our exact mathematical compass, returning the derivative of w^2.
- `w = w - learning_rate * gradient:` The Gradient Descent update rule. Notice there is no `if/else` statement checking if the error improved. The math guarantees we are stepping in the correct direction.
"""
def get_gradient(w: float) -> float:
    """Returns the derivative of the loss function L = w^2"""
    return 2 * w

# Example weights
w = 10.0 
learning_rate = 0.1
epochs = 50

print(f"Starting weight: {w}, Starting Loss: {w**2}")

for epoch in range(epochs):
    # Gradient for the current weight
    gradient = get_gradient(w)
    # Gradient Descent formula
    w = w - learning_rate * gradient
    # Current epoch, weight, and loss (w^2)
    print(f"Epoch {epoch + 1}: Weight = {w:.4f}, Loss = {w**2:.4f}")