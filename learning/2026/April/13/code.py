"""
Code Explanation:
- `get_gradient(...)`: Implements the Chain Rule formula `2 * x * (y_hat - y)`. This exact equation points the weight in the exact direction needed to reduce error.
- The Loop: Notice the clear separation of the Forward Pass (`forward_pass`), Loss Calculation (`calculate_loss`), and Backpropagation (`get_gradient`). This mirrors exactly how PyTorch structures its training loops!
"""
def forward_pass(x: float, w: float) -> float:
    """the prediction (y_hat) of our model."""
    return w * x

def calculate_loss(y: float, y_hat: float) -> float:
    """the squared error loss."""
    return (y_hat - y) ** 2

def get_gradient(x: float, y: float, y_hat: float) -> float:
    """Uses the Chain Rule to calculate how much to change the weight."""
    return 2 * x * (y_hat - y)

# House that is 2000 SqFt (x = 2.0). True price is $100k (y = 100.0).
x = 2.0
y = 100.0

w = 1.0 # Initial weight (price per SqFt)
learning_rate = 0.01
epochs = 125

for epoch in range(epochs):
    y_hat = forward_pass(x, w) 
    loss = calculate_loss(y, y_hat)
    gradient = get_gradient(x, y, y_hat)
    w = w - learning_rate * gradient
    print(f"Epoch {epoch + 1}: Weight = {w:.4f}, Loss = {loss:.8f}")