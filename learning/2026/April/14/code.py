"""
Code Explanation:
- `forward_pass(...)`: Updated to include the bias parameter. Without this, the bias gradient has no effect!
- `get_gradient_w` vs `get_gradient_b`: We compute two separate partial derivatives. The weight gradient is scaled by `x`, while the bias gradient is scaled by `1`.
- Both parameters are updated simultaneously using their respective gradients and the shared learning rate.
"""
def forward_pass(x: float, w: float, b: float) -> float:
    """the prediction (y_hat) of our model."""
    return (w * x) + b

def calculate_loss(y: float, y_hat: float) -> float:
    """the squared error loss."""
    return (y_hat - y) ** 2

def get_gradient_w(x: float, y: float, y_hat: float) -> float:
    """Uses the Chain Rule to calculate how much to change the weight."""
    return 2 * x * (y_hat - y)

def get_gradient_b(x: float, y: float, y_hat: float) -> float:
    """Uses the Chain Rule to calculate how much to change the bias."""
    return 2 * (y_hat - y)

# House that is 2000 SqFt (x = 2.0). True price is $150k (y = 150.0).
x = 2.0
y = 200.0

# Initial random parameters
w = 1.0 
b = 1.0
learning_rate = 0.05
epochs = 200


for epoch in range(epochs):
    y_hat = forward_pass(x, w, b) 
    loss = calculate_loss(y, y_hat)
    w_gradient = get_gradient_w(x, y, y_hat)
    b_gradient = get_gradient_b(x, y, y_hat)
    w = w - learning_rate * w_gradient
    b = b - learning_rate * b_gradient
    print(f"Epoch {epoch + 1}: Weight = {w:.4f}, Bias = {b:.4f}, Loss = {loss:.8f}")