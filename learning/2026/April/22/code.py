"""
Code Explanation:
This is the updated gradient descent math. We isolate the penalty gradient, explicitly ensure we divide it by N so it scales properly with the dataset, and add it to our base weight gradients. The bias is left completely unpenalized. 
"""

import numpy as np

def get_regularized_gradients(X: np.ndarray, y: np.ndarray, y_hat: np.ndarray, w: np.ndarray, lambda_param: float) -> tuple[np.ndarray, float]:
    """
    Calculates the gradients for w and b, including the L2 (Ridge) penalty.
    """
    N = len(y)
    error_vector = y_hat - y
    
    b_gradient = (2 / N) * np.sum(error_vector)
    w_gradients_base = (2 / N) * np.dot(X.T, error_vector)
    penalty_gradient = ((2 * lambda_param) / N) * w
    w_gradients_final = w_gradients_base + penalty_gradient
    
    return w_gradients_final, b_gradient

# --- A Quick Test ---
N = 100
w_massive = np.array([200.0, 150.0])
w_gradients_base = np.array([-5.0, -2.0])

np.random.seed(42)  # For reproducibility

lambda_param = 100
w_final, b = get_regularized_gradients(
    X=np.random.rand(N, 2),
    y=np.random.rand(N),
    y_hat=np.random.rand(N),
    w=w_massive,
    lambda_param=lambda_param
)
print("Base Gradients (without penalty):", w_gradients_base)
print("Final Gradients (with L2 penalty) for Lambda =", lambda_param, ":", w_final)
print("Bias Gradient:", b)