"""
Code Explanation:
This script implements Binary Cross-Entropy (Log Loss), the required objective function for Logistic Regression. It utilizes full NumPy vectorization and includes an epsilon clipping safeguard to prevent divide-by-zero crashes when calculating logarithms.
"""
import numpy as np

def binary_cross_entropy(y_true, y_pred):
    # Clip predictions to avoid log(0)
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
    
    # Calculate binary cross-entropy loss
    loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

y_true = np.array([1, 0, 1])

y_perfect = np.array([0.99, 0.01, 0.99])
print("Loss (Near Perfect):", binary_cross_entropy(y_true, y_perfect))

y_arrogant_and_wrong = np.array([0.0, 1.0, 0.0])
print("Loss (Arrogant):", binary_cross_entropy(y_true, y_arrogant_and_wrong))